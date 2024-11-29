import React from 'react';
import { DndContext, useDroppable, useDraggable, closestCenter } from '@dnd-kit/core';
import { arrayMove, SortableContext, rectSortingStrategy, useSortable } from '@dnd-kit/sortable';
import { CSS } from "@dnd-kit/utilities";

import crm_style from './crm_table.module.css'

import { findContainerId, findDraggableItemInContainer } from './crm_helpers/helpers';



export default function CrmTables() {
  const [columns, setColumns] = React.useState(crmTableData)
  const [createMode, setCreateMode] = React.useState(false)
  
  const handleDragEnd = (event) => {
    const { active, over } = event;
    if (active.id !== over?.id) {
      if (active.data.current.type === 'board' && over.data.current.type === 'board') {
        const oldIndex = columns.findIndex((column) => column.id === active.id);
        const newIndex = columns.findIndex((column) => column.id === over.id);
        const updatedColumns = [...columns];
        const [movedColumn] = updatedColumns.splice(oldIndex, 1);
        updatedColumns.splice(newIndex, 0, movedColumn);
        setColumns(updatedColumns);
      }
      else if (active.data.current.type === 'client') {
        const currentItem = findDraggableItemInContainer(columns, active.id);
        setColumns((prevColumns) => 
        prevColumns.map((column) => {
          if (column.id === active.data.current.columnId) {
            return {
              ...column,
              clients: column.clients.filter((client) => client.id !== currentItem.id)
            }
          }else if (column.id === over.id) {
            return {
              ...column,
              clients: [...column.clients, currentItem]
            }
          }
          return column
        }))
      }
    }
  };

  const handleCretaeTable = () => {
    console.log('created')
  }

  return (
    <DndContext onDragEnd={handleDragEnd}>
      <section className={crm_style.crmTable}>
        {columns.map((column) => (
          <DroppableColumn key={column.id} id={column.id} columnId={column.id}>
            <DraggableColumn id={column.id} boardName={column.name} clientsData={column.clients}/>
          </DroppableColumn>
        ))}
        <div className={crm_style.createTable} onClick={handleCretaeTable}>
          <h4>Создать новый этап</h4>
        </div>
      </section>
    </DndContext>
  )
}

function DroppableColumn({ id, children, columnId }) {
  const { setNodeRef } = useDroppable({
    id,
    data: {type: 'board'}
  });

  return (
    <div ref={setNodeRef} className={crm_style.boardItem}>
      {children}
    </div>
  );
}

function DraggableColumn({ id, boardName, clientsData }) {
  const { attributes, listeners, setNodeRef, transform } = useDraggable({
    id,
    data: {type: 'board'}
  })
  const style = {
    transform: transform
      ? `translate3d(${transform.x}px, ${transform.y}px, 0)`
      : undefined,
    backgroundColor: "lightblue",
    width: '100%',
    height: '100%'
  }
  return (
    <div ref={setNodeRef} className={crm_style.boardItem} style={style} {...attributes} {...listeners}>
      <div className={crm_style.tableHeader}>
        <h4>{boardName}</h4>
      </div>
      {id === 1 && (
        <div className={crm_style.createClient}>Создать клиента</div>
      )}
      {clientsData.map((client, index) => (
        <DraggableClient key={client.id} client={client} columnId={id} index={index}/>
      ))}
    </div>
  )
}


function DraggableClient({ client, columnId, index }) {
  const { attributes, listeners, setNodeRef, transform } = useDraggable({
    id: client.id,
    data: { type: 'client', columnId, index },
    index
  })
  const style = {
    transform: transform ? `translate3d(${transform.x}px, ${transform.y}px, 0)` : undefined,
  }

  return (
    <div ref={setNodeRef} className={crm_style.clientData} style={style} {...attributes} {...listeners}>
      {client.name}
    </div>
  )
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

const columnData = [
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