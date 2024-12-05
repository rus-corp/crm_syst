import { createSlice } from "@reduxjs/toolkit";

const clientSlice = createSlice({
  name: 'clientSlug',
  initialState: {
    clientSlug: ''
  },
  reducers: {
    setClientSlug(state, action) {
      state.slug = action.payload
    }
  }
})

export const { setClientSlug } = clientSlice.actions
export default clientSlice.reducer