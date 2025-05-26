import React from 'react';
import backImg from '../../assets/app_img/Illustration.png';
import style from './login.module.css';
import { CreateItemInput } from '../../ui';
import { LoginBtn } from '../../ui';

export default function LoginComponent({ onSubmit, loginError }) {
  const [loginData, setLoginData] = React.useState({
    email: '',
    password: ''
  });
  const handleInputChange = (name, value) => {
    setLoginData({
      ...loginData,
      [name]: value
    });
  };
  const handleLogin = async (e) => {
    e.preventDefault();
    onSubmit(loginData);
  };

  return (
    <section className={style.loginSection}>
      <div className={style.loginBlock}>
        <div className={style.leftSide}>
          <div className={style.blockTitle}>
            <h1>Астроверты</h1>
          </div>
          <img src={backImg} alt="back" />
        </div>
        <div className={style.rightSide}>
          <div className={style.rigthWrapper}>
            <div className={style.rightBlockTitle}>
              <h4>Войти в систему</h4>
            </div>
            <form className={style.loginForm} onSubmit={handleLogin}>
              <div className={style.formFields}>
                <div className={style.fieldItem}>
                  <CreateItemInput
                  fieldTitle={'Email'}
                  fieldWidth={'34rem'}
                  fieldType={'email'}
                  fieldName={'email'}
                  value={loginData.email}
                  changeFunc={handleInputChange}
                  />
                </div>
                <div className={style.fieldItem}>
                  <CreateItemInput
                  fieldTitle={'Пароль'}
                  fieldWidth={'34rem'}
                  fieldType={'password'}
                  fieldName={'password'}
                  value={loginData.password}
                  changeFunc={handleInputChange}
                  />
                </div>
              </div>
              <LoginBtn />
            </form>
            <p style={{color: "red", display: loginError ? "block" : "none"}}>Не верные email или пароль</p>
          </div>
        </div>
      </div>
    </section>
  );
}