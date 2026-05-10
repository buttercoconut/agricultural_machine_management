import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Table, Button, Modal, Form } from 'react-bootstrap';

const RentalManagement = () => {
  const [rentals, setRentals] = useState([]);
  const [show, setShow] = useState(false);
  const [form, setForm] = useState({ machine_id: '', renter_id: '', start_date: '', end_date: '', daily_rate: '' });

  useEffect(() => {
    fetchRentals();
  }, []);

  const fetchRentals = async () => {
    const res = await axios.get('/api/rental');
    setRentals(res.data);
  };

  const handleSubmit = async () => {
    await axios.post('/api/rental', form);
    setShow(false);
    fetchRentals();
  };

  return (
    <div>
      <h2>Rental Management</h2>
      <Button onClick={() => setShow(true)}>Add Rental</Button>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Machine ID</th>
            <th>Renter ID</th>
            <th>Start Date</th>
            <th>End Date</th>
            <th>Daily Rate</th>
          </tr>
        </thead>
        <tbody>
          {rentals.map(r => (
            <tr key={r.id}>
              <td>{r.id}</td>
              <td>{r.machine_id}</td>
              <td>{r.renter_id}</td>
              <td>{r.start_date}</td>
              <td>{r.end_date}</td>
              <td>{r.daily_rate}</td>
            </tr>
          ))}
        </tbody>
      </Table>

      <Modal show={show} onHide={() => setShow(false)}>
        <Modal.Header closeButton>
          <Modal.Title>Add Rental</Modal.Title>
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
            <Form.Group controlId="renter_id">
              <Form.Label>Renter ID</Form.Label>
              <Form.Control
                type="number"
                value={form.renter_id}
                onChange={e => setForm({ ...form, renter_id: e.target.value })}
              />
            </Form.Group>
            <Form.Group controlId="start_date">
              <Form.Label>Start Date</Form.Label>
              <Form.Control
                type="date"
                value={form.start_date}
                onChange={e => setForm({ ...form, start_date: e.target.value })}
              />
            </Form.Group>
            <Form.Group controlId="end_date">
              <Form.Label>End Date</Form.Label>
              <Form.Control
                type="date"
                value={form.end_date}
                onChange={e => setForm({ ...form, end_date: e.target.value })}
              />
            </Form.Group>
            <Form.Group controlId="daily_rate">
              <Form.Label>Daily Rate</Form.Label>
              <Form.Control
                type="number"
                step="0.01"
                value={form.daily_rate}
                onChange={e => setForm({ ...form, daily_rate: e.target.value })}
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

export default RentalManagement;
