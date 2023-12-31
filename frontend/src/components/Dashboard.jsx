
import { useState} from 'react'
import { useSelector } from 'react-redux'
import Question from './Question'
import TableView from './TableView'
import { dataData, statusData, authedUser } from '../reducers/data';
import { useParams } from 'react-router-dom';
import NavTop from './Nav';
import LoadingBar from 'react-redux-loading-bar'




function Dashboard(){
    let { category } = useParams();
    category = category ? category : "category"

    

    const data = useSelector(dataData)
    const isLoading = useSelector(statusData)
    
    let data_current = data[category] ? data[category] : []
    const current_user = useSelector(authedUser)
    console.log(current_user)

  

    
    
    // const [optimizedView, setOptimizedView] = useState(true)
    const [searchInput, handleSearchChange] = useState("")


        return(
          <>
          <LoadingBar/>
          <NavTop/>
            <div className='dashboard'>
                {(category == "category")? <div className='questions'>
                 
                    <div key="search-bar" className="form-group row">
                      <div className="col-sm-10">
                        <input type='text' className="form-control" id={`colFormLabelSearchBar`} value={searchInput} placeholder="Search..." onChange={(e)=>handleSearchChange(e.target.value)}/>
                      </div>
                    </div>
                    {data_current.filter(dat=> dat.name.toLowerCase().includes(searchInput.toLowerCase())
                    ).map(cat => cat.name != "user" ? <Question key={cat.id} id={cat.id} table={category} data={cat}/>
                    : current_user && current_user.is_superuser && <Question key={cat.id} id={cat.id} table={category} data={cat}/>
                  )}</div>
                :
                <TableView key={category} table={category}/>
                }
            </div>
            </>)
}

export default Dashboard
