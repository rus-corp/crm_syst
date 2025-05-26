import React from 'react';
import { useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import style from './styles/crm_page.module.css'

import { MainMenu } from '../../modules';
import { CrmTable } from '../../modules/crm_module';




export default function CrmPage() {
  const user = useSelector(state => state.user.userData);
  console.log(user)
  const navigation = useNavigate();
  React.useEffect(() => {
    if (!user) {
      navigation('/login');
    }
  }, [user])
  return(
    <div className="container">
      <div className={style.crmPage}>
      <MainMenu />
      <CrmTable />
      </div>
    </div>
  );
}