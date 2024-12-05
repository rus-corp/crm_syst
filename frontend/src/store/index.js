import { configureStore } from '@reduxjs/toolkit'
import ClientReducer from './clientSlice'

export default configureStore({
  reducer: {
    client: ClientReducer,
  }
})