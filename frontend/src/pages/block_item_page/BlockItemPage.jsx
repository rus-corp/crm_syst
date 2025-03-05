import React from 'react';
import { MainMenu } from '../../modules';
import { useParams } from 'react-router-dom';
import { StaffBlockComponent, ExpenseBlockComponent } from '../../ui';



export default function BlockItemPage() {
  const { type } = useParams()
  const renderComponent = () => {
    switch (type) {
      case 'staff':
        return <StaffBlockComponent />
      case 'expenses':
        return <ExpenseBlockComponent />
      case 'room':
        return <CreateRoom />
      default:
        return <CreateStaff />
    }
  }
  return(
    <div className="container hotels">
      <MainMenu />
      {renderComponent()}
    </div>
  );
}