import React from 'react';
import { MainMenu } from '../../modules';
import { useParams } from 'react-router-dom';
import { CreateStaff, CreateExpense } from '../../ui';



export default function CreateItemPage() {
  const { type } = useParams()
  const renderComponent = () => {
    switch (type) {
      case 'staff':
        return <CreateStaff />
      case 'expenses':
        return <CreateExpense />
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