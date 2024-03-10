import { useLocation } from "react-router-dom"


const TitleSummaryPage = () => {
  const location = useLocation();
  console.log(location);
  return (
    <div>
      <h1>Title : {location.state.title}</h1>
      <p>
        Summary: {location.state.summary[0].summary_text}
      </p>
    </div>
  )
}

export default TitleSummaryPage
