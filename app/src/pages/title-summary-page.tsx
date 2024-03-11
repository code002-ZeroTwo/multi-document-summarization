import { Button } from "@/ui/button";
import { Link, useLocation, useNavigate } from "react-router-dom"


const TitleSummaryPage = () => {
  const location = useLocation();

  return (
    <div>
      <Link to='/'>
      <Button>Back to Home Page</Button>
      </Link>
      <h1 className=" text-[30px] mt-[2rem] border-[10px] border-primary"><strong>Title</strong> : {location.state.title}</h1>
      <h2 className='text-[28px] border-[10px] border-primary my-[-10px]'><strong>Description</strong> : {location.state.description}</h2>
      <p className="text-[26px] border-[10px] border-primary">
        <strong>Summary</strong> : {location.state.summary[0].summary_text}
      </p>
    </div>
  )
}

export default TitleSummaryPage
