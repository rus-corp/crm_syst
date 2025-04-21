import { configureStore } from '@reduxjs/toolkit'
import ClientReducer from './clientSlice'
import ProgramReducer from './programSlice'

export default configureStore({
  reducer: {
    client: ClientReducer,
    program: ProgramReducer
  }
})