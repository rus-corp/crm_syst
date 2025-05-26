import { configureStore } from '@reduxjs/toolkit'
import ClientReducer from './clientSlice'
import ProgramReducer from './programSlice'
import userReducer from './userSlice'

export default configureStore({
  reducer: {
    client: ClientReducer,
    program: ProgramReducer,
    user: userReducer
  }
})