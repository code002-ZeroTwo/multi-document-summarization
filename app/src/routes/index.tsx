import Home from "@/pages/home"
import TitleSummaryPage from "@/pages/title-summary-page"
import {Route, Routes} from "react-router-dom"

const RouteLayout = () => {
  return (
    <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/title-page-summary" element={<TitleSummaryPage/>} />
    </Routes>
  )
}

export default RouteLayout
