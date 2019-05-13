import React from 'react';
import './App.css';
import { Layout, Menu } from 'antd';
import { Route, Switch } from 'react-router-dom';

const { Header, Content, Footer } = Layout;

function App () {
  return (
    <div className="App">
      <Header>
        
      </Header>
      <Content>
        <Switch>
          <Route to="/emprestimos" exact component={} />
          <Route to="/cobrancas" exact component={} />
        </Switch>
      </Content>
      <Footer></Footer>
    </div>
  );
}

export default App;
