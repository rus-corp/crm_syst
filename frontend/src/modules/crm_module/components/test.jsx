import React from 'react';
import { DndContext, useDroppable, useDraggable, closestCenter } from '@dnd-kit/core';
import { arrayMove, SortableContext, verticalListSortingStrategy, useSortable } from '@dnd-kit/sortable';

import crm_style from './crm_table.module.css'

import { findContainerId, findDraggableItemInContainer } from './crm_helpers/helpers';







export default function CrmTables() {
  const [containers, setContainers] = React.useState(crmTableData);

  const handleDragEnd = (event) => {
    const { active, over } = event;
    if (!over) return;

    const isTableDrag = containers.some(container => container.id === active.id)
    if (isTableDrag) {
      const oldIndex = containers.findIndex(container => container.id === active.id)
      const newIndex = containers.findIndex(container => container.id === over.id)
      if (oldIndex !== newIndex) {
        setContainers((prevContainers) => arrayMove(prevContainers, oldIndex, newIndex))
      }
    } else {
      const sourceContainerId = findContainerId(containers, active.id);
      const targetContainerId = over.id;
      if (sourceContainerId && sourceContainerId !== targetContainerId) {
        const currentItem = findDraggableItemInContainer(containers, active.id);
        setContainers((prevContainers) =>
          prevContainers.map((container) => {
            if (container.id === sourceContainerId) {
              return {
                ...container,
                clients: container.clients.filter((client) => client.id !== currentItem.id),
              };
            } else if (container.id === targetContainerId) {
              return {
                ...container,
                clients: [...container.clients, currentItem],
              };
            }
            return container;
          })
        );
      }

    }
  };

  return (
    <DndContext onDragEnd={handleDragEnd} collisionDetection={closestCenter}>
      <SortableContext items={containers.map(container => container.id)} strategy={verticalListSortingStrategy}>
        <section className={crm_style.crmTable}>
          {containers.map((table) => (
            <CrmTableItem key={table.id}
            id={table.id}
            clients={table.clients}
            boardName={table.name}
            />
          ))}
        </section>
      </SortableContext>
    </DndContext>
  );
}


function CrmTableItem ({ id, clients, boardName }) {
  const { isOver, setNodeRef: setDropNodeRef } = useDroppable({
    id,
  });
  const { attributes, listeners, setNodeRef: setDragNodeRef, transform } = useSortable({
    id,
  })

  const style = {
    backgroundColor: isOver ? 'lightgreen' : 'white',
    transform: transform ? `translate3d(${transform.x}px, ${transform.y}px, 0)` : undefined,
    transition: '.5s'
    // padding: '16px',
    // border: '2px dashed gray',
    // minHeight: '100px',
    // width: '200px',
  };

  return (
    <div
    ref={(node) => {
      setDropNodeRef(node);
      setDragNodeRef(node)
    }}
    className={crm_style.boardItem}
    style={style}>
      <div className={crm_style.tableHeader}>
        <h4>{boardName}</h4>
      </div>
      {id === 1 && (
        <div className={crm_style.createClient}>Создать клиента</div>
      )}
      <div className={crm_style.tableContent}>
        {clients.map((item) => (
          <Client
          key={item.id}
          id={item.id}
          clientName={item.name}
          clientLastName={item.last_name}
          clientEmail={item.email}
          clientPhone={item.phone}
          />
        ))}
      </div>
    </div>
  );
}


function Client ({ id, clientName, clientLastName, clientEmail, clientPhone, children }) {
  const { attributes, listeners, setNodeRef, transform } = useDraggable({
    id,
  })
  const style = {
    transform: transform ? `translate3d(${transform.x}px, ${transform.y}px, 0)` : undefined,
    // padding: '8px',
    // border: '1px solid black',
    // margin: '4px',
    // backgroundColor: 'lightgray',
  };

  return (
    <div className={crm_style.clientData}
    ref={setNodeRef}
    {...listeners}
    {...attributes}
    style={style}
    >
      <div className={crm_style.clientName}>
        <p>{clientName}</p>
        <p>{clientLastName}</p>
      </div>
      <div className={crm_style.clientProgram}>
        <h6>Astor</h6>
      </div>
      <div className={crm_style.clientDate}>
        <p>23.08.2023</p>
      </div>
      {children}
    </div>
  );
}




const crmTableData = [
  {
    "id": 1,
    "name": "Новый клиент",
    "sequence_number": 1,
    "clients": [
      {
        "id": 13,
        "last_name": "Смирнов",
        "name": "Юрий",
        "second_name": "Владимирович",
        "phone": "89289048086",
        "email": "caramelcuddle@gmail.com"
      },
      {
        "id": 14,
        "last_name": "Смирнова",
        "name": "Валерия",
        "second_name": "Геннадьевна",
        "phone": "89289048085",
        "email": "caramelcuddle1@gmail.com"
      },
      {
        "id": 15,
        "last_name": "Гудкова",
        "name": "Лилия",
        "second_name": "Наядовна",
        "phone": "79165291665",
        "email": "Lilia.gudkova@rambler.ru"
      },
      {
        "id": 16,
        "last_name": "Захваткина",
        "name": "Ольга",
        "second_name": "Александровна",
        "phone": "89165291665",
        "email": "kontorka@bk.ru"
      },
      {
        "id": 17,
        "last_name": "Зинкина",
        "name": "Галина",
        "second_name": "Владимировна",
        "phone": "79031367595",
        "email": "Zinkina@me.com"
      },
      {
        "id": 18,
        "last_name": "Щербакова",
        "name": "Наталья",
        "second_name": "Николаевна",
        "phone": "79060491010",
        "email": "n.scherbakova@list.ru"
      },
      {
        "id": 19,
        "last_name": "Петухова",
        "name": "Ольга",
        "second_name": "Андреевна",
        "phone": "9",
        "email": "n.scherbakova1@list.ru"
      },
      {
        "id": 20,
        "last_name": "Шифрина",
        "name": "Ольга",
        "second_name": "Анатольевна",
        "phone": "79671726826",
        "email": "o_shifrina@mail.ru"
      },
      {
        "id": 21,
        "last_name": "Жуковский",
        "name": "Александр",
        "second_name": "Викторович",
        "phone": "79853596687",
        "email": "zav2003@bk.ru"
      },
      {
        "id": 22,
        "last_name": "Жуковская",
        "name": "Полина",
        "second_name": "Александровна",
        "phone": "79853596688",
        "email": "zav2004@bk.ru"
      },
      {
        "id": 23,
        "last_name": "Жуковский",
        "name": "Константин",
        "second_name": "Александрович",
        "phone": "79853596689",
        "email": "zav2005@bk.ru"
      },
      {
        "id": 24,
        "last_name": "Голдар",
        "name": "Наталья",
        "second_name": "Андреевна",
        "phone": "79853596690",
        "email": "zav2006@bk.ru"
      },
      {
        "id": 25,
        "last_name": "Цепилов",
        "name": "Владислав",
        "second_name": "Александрович",
        "phone": "79775784890",
        "email": "fickleprogger@gmail.com"
      },
      {
        "id": 26,
        "last_name": "Сапронова",
        "name": "Екатерина",
        "second_name": "Игоревна",
        "phone": "79253851506",
        "email": "fickleprogger1@gmail.com"
      },
      {
        "id": 27,
        "last_name": "Осадчая",
        "name": "Анастасия",
        "second_name": "Николаевна",
        "phone": "89268591115",
        "email": "melb2@yandex.ru"
      },
      {
        "id": 28,
        "last_name": "Ларькина",
        "name": "Ольга",
        "second_name": "Юрьевна",
        "phone": "89268591116",
        "email": "melb3@yandex.ru"
      },
      {
        "id": 29,
        "last_name": "Афанасьева",
        "name": "Анастасия",
        "second_name": "Олеговна",
        "phone": "79204639687",
        "email": "nastya_afa@icloud.com"
      },
      {
        "id": 30,
        "last_name": "Данилюк",
        "name": "Олег",
        "second_name": "Викторович",
        "phone": "89267089708",
        "email": "ol3d@yandex.ru"
      },
      {
        "id": 31,
        "last_name": "Власова",
        "name": "Татьяна",
        "second_name": "Борисовна",
        "phone": "89162299892",
        "email": "t.b.vlasova@mail.ru"
      },
      {
        "id": 32,
        "last_name": "Зарипов",
        "name": "Тимур",
        "second_name": "Андреевич",
        "phone": "79272466873",
        "email": "timzar9@gmail.com"
      },
      {
        "id": 33,
        "last_name": "Зарипова",
        "name": "Айгуль",
        "second_name": "Рашидовна",
        "phone": "79172889962",
        "email": "Zaraigul11@yandex.ru"
      },
      {
        "id": 34,
        "last_name": "Дунин",
        "name": "Максим",
        "second_name": "Николаевич",
        "phone": "79136217927",
        "email": "dmn99@mail.ru"
      },
      {
        "id": 35,
        "last_name": "Жильцов",
        "name": "Илья",
        "second_name": "Евгеньевич",
        "phone": "79166208867",
        "email": "Frostsaberr@gmail.com"
      },
      {
        "id": 36,
        "last_name": "Торкунова",
        "name": "Алина",
        "second_name": "Анатольевна",
        "phone": "89168050588",
        "email": "Alina.crypto369@gmail.com"
      },
      {
        "id": 37,
        "last_name": "Ершов",
        "name": "Александр",
        "second_name": "Юрьевич",
        "phone": "79215639144",
        "email": "aleks.ershov85@gmail.com"
      }
    ]
  },
  {
    "id": 2,
    "name": "Сделан звонок",
    "sequence_number": 2,
    "clients": []
  },
  {
    "id": 4,
    "name": "Думает",
    "sequence_number": 3,
    "clients": []
  },
  {
    "id": 3,
    "name": "Заключен договор",
    "sequence_number": 4,
    "clients": []
  }
]




      {/* {boardList.sort(sortCards).map(board => 
      <div className={crm_style.boardItem} key={board.id}
      >
        <CrmTableItem key={board.id}
        boardId={board.id}
        tableName={board.name}
        clientData={board.clients}
        moveClient={moveClient}
        />
      </div>
      )}
      <div className={crm_style.createTable}>
        <h5>Создать новую колонку</h5>
      </div> */}