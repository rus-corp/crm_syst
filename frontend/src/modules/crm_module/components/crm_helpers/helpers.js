

export function findContainerId(containers, draggableId) {
  const container  = containers.find((cont) =>
  cont.clients.some((item) => item.id === draggableId))
  return container ? container.id : null
}


export function findDraggableItemInContainer(containers, draggableId) {
  for (const container of containers) {
    const client = container.clients.find((item) => item.id === draggableId)
    if (client) {
      return client
    }
  }
  return null
}