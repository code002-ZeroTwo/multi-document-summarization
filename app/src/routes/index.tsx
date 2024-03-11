import Home from "@/pages/home"
import Loading from "@/pages/loading"
import TitleSummaryPage from "@/pages/title-summary-page"
import {Route, Routes} from "react-router-dom"

const RouteLayout = () => {
  return (
    <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/title-page-summary" element={<TitleSummaryPage/>} />
        <Route path="/loading" element={<Loading></Loading>} />
    </Routes>
  )
}

export default RouteLayout
