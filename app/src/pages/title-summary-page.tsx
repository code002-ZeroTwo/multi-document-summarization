import { useLocation } from "react-router-dom"


const TitleSummaryPage = () => {
  const location = useLocation();
  console.log(location);
  return (
    <div>
      <h1>Summary for the title : {location.state.title}</h1>
    </div>
  )
}

export default TitleSummaryPage
