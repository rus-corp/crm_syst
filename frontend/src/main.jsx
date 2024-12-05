import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { RouterProvider} from 'react-router-dom'
import { router } from './routers/router.jsx'
import store from './store/index.js'
import { Provider } from 'react-redux'

import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  // <StrictMode>
  <Provider store={store}>
    <RouterProvider router={router} future={{ v7_startTransition: true }}/>
  </Provider>
  // </StrictMode>,
)
