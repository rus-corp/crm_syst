import React from 'react';
import { jwtDecode } from "jwt-decode";
import { useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { LoginComponent } from '../../modules/client_module';
import { setUser } from '../../store/userSlice';

import { authLogin } from '../../api';

export default function LoginPage() {
  const [loginError, setLoginError] = React.useState(false);
  const navigation = useNavigate()
  const dispatch = useDispatch()
  const handleSubmit = async (userData) => {
    const params = new URLSearchParams()
    params.append('username', userData.email)
    params.append('password', userData.password)
    try {
      const response = await authLogin(params)
      if (response.status === 201) {
        const accessToken = response.data.access_token
        const refreshToken = response.data.refresh_token
        const decodeToken = jwtDecode(accessToken)
        localStorage.setItem('accessToken', accessToken)
        dispatch(setUser({
          userData: accessToken,
          userRole: decodeToken.role,
        }))
        localStorage.setItem('refreshToken', refreshToken)
        navigation('/')
        // if(decodeToken.role === 'redactor' || decodeToken.role === 'superuser') {
        //   navigate('/bases')
        // } else if(decodeToken.role === 'client' || decodeToken.role === 'manager') {
        //   navigate('/clients')
        // }
      } else {
        setLoginError(true)
      }
    } catch(error) {
      console.error(error)
    }
  }
  return(
    <LoginComponent
    onSubmit={handleSubmit}
    loginError={loginError}
    />
  );
}