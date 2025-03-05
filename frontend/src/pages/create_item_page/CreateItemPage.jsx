import React from 'react';
import { MainMenu } from '../../modules';
import { useParams } from 'react-router-dom';
import { CreateStaff, CreateExpense } from '../../ui';



export default function CreateItemPage() {
  const { type } = useParams()
  const renderComponent = () => {
    switch (type) {
      case 'create_staff':
        return <CreateStaff />
      case 'create_expense':
        return <CreateExpense />
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