import React from 'react';
import { Form, Button, Col, Row, Input } from 'antd';
import './Emprestimo.css';


class EmprestimoForm extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      nomeEmprestimo: ''
    };

    this.handleNomeEmprestimoChange = this.handleNomeEmprestimoChange.bind(this);
  };

  handleSubmit = (event) => {
    event.preventDefault();
  };

  handleNomeEmprestimoChange = (event) => {
    this.props.form.setFieldsValue({ nomeEmprestimo: event.target.value });
    this.setState({ nomeEmprestimo: this.props.form.getFieldValue('nomeEmprestimo') });
  }

  render () {
    const { getFieldDecorator } = this.props.form;

    return (
      <Row>
        <h1>Criar Emprestimo</h1>
        <Col span={12} offset={6} className="form-column">
          <Form onSubmit={this.handleSubmit} className="emprestimo-form">
            <Form.Item>
              {
                getFieldDecorator('nomeEmprestimo', {
                  rules: [{ required: true, message: 'Insira um nome para o emprestimo' }]
                })(
                  <Input type="text" placeholder="nome do emprestimo" onChange={this.handleNomeEmprestimoChange} />
                )
              }
            </Form.Item>
            <Button type="primary" htmlType="submit">Criar emprestimo</Button>
          </Form>
        </Col>
      </Row>
    );
  }
}

const wrappedEmprestimoForm = Form.create({name: "EmprestimoForm"})(EmprestimoForm);

export default wrappedEmprestimoForm;