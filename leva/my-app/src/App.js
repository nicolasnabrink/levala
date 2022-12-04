import './App.css';
import React from 'react';


let companyData = [
  {
    name: 'empresa1',
    user: '1',
    logoURL: 'a',
    cnpj: '123',
    tel: '123',
    job: 'sim',
    city: 'sp',
  },
  {
    name: 'empresa2',
    user: '2',
    logoURL: 'b',
    cnpj: '456',
    tel: '456',
    job: 'nao',
    city: 'rj',
  }
]

function CompaniesTable(props) {
  const {list, onDismiss, searchTerm} = props;
  return (
    <table>
        <thead>
          <tr>
            <th>name</th>
            <th>user</th>
            <th>job</th>
            <th>logoURL</th>
          </tr>
        </thead>
        <tbody>
          {list.filter(company => company.name.toLowerCase().includes(searchTerm.toLowerCase()))
          .map((company) => (
            <tr key={company.user}>
              <td>{company.name}</td>
              <td>{company.user}</td>
              <td>{company.job}</td>
              <td>{company.logoURL}</td>
              <td>
              <Button onClick ={() => onDismiss(company.user)}>
                Dismiss
              </Button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
  );
}

function Search(props) {
  const {searchTerm, handleInputChange, children} = props;
  return (
      <form>
        {children} <input type="text" placeholder="Search by company name"
          name="searchTerm" value={searchTerm} 
          onChange={(event) => handleInputChange(event)}/>
      </form>
    );
}

function Button(props) {
  const {
    onClick,
    className='',
    children,
  } = props;

  return (
    <button
      onClick={onClick}
      className={className}
      type="button"
    >
      {children}
    </button>
  );
}

class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = { list: null };
  }

componentDidMount() {
  fetch('http://127.0.0.1:8000/api/v1/companies/')
    .then((response) => response.json())
    .then((result) => this.setState({ list: result }))
    .catch((error) => error);
}

onSearchChange(event) {
    this.setState({ searchTerm: event.target.value });
}


handleInputChange(event) {
  const target = event.target;
  const value = 
    target.type === 'checkbox' ? target.checked : target.value;
  const name = target.name;

  this.setState({
    [name]: value
  });
}

  onDismiss(id) {
    const updatedList = this.state.list.filter(item => item.user !== id);
    this.setState({ list: updatedList });
  }

  render() {
    const {list, searchTerm} = this.state;
    
    return (
      <div className="App">
        <Search
          searchTerm={searchTerm}
          handleInputChange={(e) => this.handleInputChange(e)}
        >
          Search term:
        </Search>
        <CompaniesTable  list={list} 
            onDismiss={(id) => this.onDismiss(id)}
            searchTerm={searchTerm}
            onSearchChange={(e) => this.onSearchChange(e)}
          />
      </div>
    );
  }
}


export default App;
