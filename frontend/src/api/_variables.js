import axios from 'axios';


export const urlConfig = {
  VITE_DEV_URL: import.meta.env.VITE_DEV_URL
}


export const backend = axios.create({
  baseURL: urlConfig.VITE_DEV_URL,
  headers: {
    'Content-Type': 'application/json',
  }
})

export const getHeader = (token) => {
  return (
    {'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json'}
  )
}