import React, { useState } from "react";
import axios from "axios";

const AdminUpload: React.FC = () => {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [files, setFiles] = useState<FileList | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!name || !description || !files) {
      alert("Fill all fields and upload at least one image");
      return;
    }

    const formData = new FormData();
    formData.append("name", name);
    formData.append("description", description);
    Array.from(files).forEach((file) => formData.append("files", file));

    try {
      await axios.post("http://localhost:8000/admin/upload-item", formData);
      alert("Item uploaded!");
      setName("");
      setDescription("");
      setFiles(null);
    } catch (err) {
      alert("Upload failed");
      console.error(err);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Upload New Item</h2>
      <input type="text" value={name} placeholder="Name" onChange={(e) => setName(e.target.value)} /><br />
      <textarea value={description} placeholder="Description" onChange={(e) => setDescription(e.target.value)} /><br />
      <input type="file" multiple accept="image/*" onChange={(e) => setFiles(e.target.files)} /><br />
      <button type="submit">Upload</button>
    </form>
  );
};

export default AdminUpload;
