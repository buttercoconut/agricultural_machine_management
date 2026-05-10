import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Table, Button, Modal, Form } from 'react-bootstrap';

const MaintenanceHistory = () => {
  const [histories, setHistories] = useState([]);
  const [show, setShow] = useState(false);
  const [form, setForm] = useState({ machine_id: '', maintenance_date: '', description: '', cost: '' });

  useEffect(() => {
    fetchHistories();
  }, []);

  const fetchHistories = async () => {
    const res = await axios.get('/api/maintenance');
    setHistories(res.data);
  };

  const handleSubmit = async () => {
    await axios.post('/api/maintenance', form);
    setShow(false);
    fetchHistories();
  };

  return (
    <div>
      <h2>Maintenance History</h2>
      <Button onClick={() => setShow(true)}>Add History</Button>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Machine ID</th>
            <th>Date</th>
            <th>Description</th>
            <th>Cost</th>
          </tr>
        </thead>
        <tbody>
          {histories.map(h => (
            <tr key={h.id}>
              <td>{h.id}</td>
              <td>{h.machine_id}</td>
              <td>{h.maintenance_date}</td>
              <td>{h.description}</td>
              <td>{h.cost}</td>
            </tr>
          ))}
        </tbody>
      </Table>

      <Modal show={show} onHide={() => setShow(false)}>
        <Modal.Header closeButton>
          <Modal.Title>Add Maintenance History</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form>
            <Form.Group controlId="machine_id">
              <Form.Label>Machine ID</Form.Label>
              <Form.Control
                type="number"
                value={form.machine_id}
                onChange={e => setForm({ ...form, machine_id: e.target.value })}
              />
            </Form.Group>
            <Form.Group controlId="maintenance_date">
              <Form.Label>Date</Form.Label>
              <Form.Control
                type="date"
                value={form.maintenance_date}
                onChange={e => setForm({ ...form, maintenance_date: e.target.value })}
              />
            </Form.Group>
            <Form.Group controlId="description">
              <Form.Label>Description</Form.Label>
              <Form.Control
                type="text"
                value={form.description}
                onChange={e => setForm({ ...form, description: e.target.value })}
              />
            </Form.Group>
            <Form.Group controlId="cost">
              <Form.Label>Cost</Form.Label>
              <Form.Control
                type="number"
                step="0.01"
                value={form.cost}
                onChange={e => setForm({ ...form, cost: e.target.value })}
              />
            </Form.Group>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={() => setShow(false)}>
            Close
          </Button>
          <Button variant="primary" onClick={handleSubmit}>
            Save
          </Button>
        </Modal.Footer>
      </Modal>
    </div>
  );
};

export default MaintenanceHistory;
