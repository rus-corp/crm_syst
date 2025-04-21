import { createSlice } from "@reduxjs/toolkit";

const programSlice = createSlice({
  name: 'programSlice',
  initialState: {
    programStartDate: '',
    programEndDate: '',
    clientProgram: ''
  },
  reducers: {
    setProgramData(state, action) {
      const {programStartDate, programEndDate, clientProgram} = action.payload
      state.programStartDate = programStartDate
      state.programEndDate = programEndDate
      state.clientProgram = clientProgram
    }
  }
})

export const { setProgramData } = programSlice.actions
export default programSlice.reducer