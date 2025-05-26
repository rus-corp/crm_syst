import React from 'react';

import style from './loginBtn.module.css'


export default function LoginBtn() {
  return(
    <button
      className={style.btn}
      type='submit'
      // onClick={clicked}
      >Войти</button>
  );
}