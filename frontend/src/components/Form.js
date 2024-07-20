import React, { useState, setTxt } from "react";
import axios from "axios";

function Form() {

  const [formData, setFormData] = useState({
    name: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/formSubs/", formData);
      console.log("Form data submitted successfully:", response.data);
    } catch (error) {
      console.error("Error submitting form data:", error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input
          type='text'
          name='name'
          value={formData.name}
          onChange={handleChange}
        />
      </label>
      <button type='submit'>Submit</button>
    </form>
  );
}
export default Form;