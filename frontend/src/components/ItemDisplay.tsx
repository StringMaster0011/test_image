import React, { useState } from "react";
import axios from "axios";
import { Item } from "../types.ts";

const ItemDisplay: React.FC = () => {
  const [itemId, setItemId] = useState("");
  const [item, setItem] = useState<Item | null>(null);

  const fetchItem = async () => {
    try {
      const res = await axios.get<Item>(`http://localhost:8000/items/${itemId}`);
      setItem(res.data);
    } catch {
      alert("Item not found");
      setItem(null);
    }
  };

  return (
    <div>
      <h2>View Item</h2>
      <input type="number" value={itemId} onChange={(e) => setItemId(e.target.value)} placeholder="Enter Item ID" />
      <button onClick={fetchItem}>Fetch</button>
      {item && (
        <div>
          <h3>{item.name}</h3>
          <p>{item.description}</p>
          <div style={{ display: "flex", flexWrap: "wrap", gap: "10px" }}>
            {item.images.map((url, i) => (
              <img key={i} src={url} alt={`img-${i}`} width={150} />
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default ItemDisplay;
