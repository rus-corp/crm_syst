export const cleanData = (data) => {
  return data.filter(item => item.room_type && item.room_price > 0)
};