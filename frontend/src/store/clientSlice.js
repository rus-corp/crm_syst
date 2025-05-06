import { createSlice } from "@reduxjs/toolkit";

const clientSlice = createSlice({
  name: 'clientSlug',
  initialState: {
    clientSlug: ''
  },
  reducers: {
    setClientSlug(state, action) {
      state.clientSlug = action.payload
    }
  }
})

export const { setClientSlug } = clientSlice.actions
export default clientSlice.reducer