import React from 'react';
import { Table, Row, Col, Button } from 'antd';
import './Emprestimo.css';
import { Link } from 'react-router-dom';


class Emprestimos extends React.Component {

  constructor(props) {
    super(props);
    this.state = { emprestimos: {} };
  }

  render () {

    const { Column } = Table;

    return (
      <Row>
        <Col span={12} offset={6}>
          <Table dataSource={this.state.emprestimos.map(emprestimo => {
            return {
              key: emprestimo.id,
              name: emprestimo.nomeEmprestimo
            }
          })} title={() => 'Emprestimos'}>
            <Column align={'center'} title="Emprestimo" dataIndex="emprestimo" key="emprestimo" />
          </Table>
          <Col span={12} offset={6}>
            <Button type="primary" className="emprestimo-create-button">
              <Link to={{ pathname: '/emprestimos/criar' }}>
                Criar emprestimo
              </Link>
            </Button>
          </Col>
        </Col>
      </Row>
    );
  }
}

export default Emprestimos;