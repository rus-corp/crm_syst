import { createSlice } from "@reduxjs/toolkit";
import { jwtDecode } from "jwt-decode";


const getUserFromToken = () => {
  if (typeof window === 'undefined') return null;
  const accessToken = localStorage.getItem('accessToken');
  if (!accessToken) return null;
  try {
    return jwtDecode(accessToken);
  } catch (error) {
    console.error('Failed to decode token:', error);
    return null;
  }
}


const initialState = {
  userData: getUserFromToken(),
  userRole: null
}

const userSlice = createSlice({
  name: 'userData',
  initialState,
  reducers: {
    setUser(state, action) {
      const { userData, userRole } = action.payload;
      state.userData = userData;
      state.userRole = userRole;
    },
    logoutUser(state) {
      state.user = null;
      state.userRole = null;
    },
  }
})

export const { setUser, logoutUser } = userSlice.actions
export default userSlice.reducer