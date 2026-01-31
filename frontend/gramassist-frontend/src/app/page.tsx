"use client"
import {useState} from 'react';
import { motion, AnimatePresence } from "framer-motion";


type Message = {
  role: "user" | "assistant";
  text: string;
};

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input,setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage: Message = { role: "user", text:input };
    setMessages((prev) => [...prev,userMessage]);
    setInput("");
    setLoading(true);

    try {
      const res = await fetch(`http://127.0.0.1:8000/ask?q=${encodeURIComponent(input)}`);
      const data = await res.json();
      const botMessage: Message = { role: "assistant", text: data.answer || "No response received." };
      setMessages((prev) => [...prev,botMessage]);
    } catch (err) {
      setMessages((prev) => [...prev, { role: "assistant", text: "Error connecting to server." }]);
    } finally {
      setLoading(false);
  }
};

return (
  <div className="flex flex-col items-center justify-center min-h-screen bg-[#d99a00] p-6">
      {/* Header */}
      <div className="flex items-center gap-3 mb-4">
        <img
          src="/grambling_logo.png" // put your image in /public folder
          alt="Grambling State University Logo"
          className="w-16 h-16 object-contain border border-blue-500"
        />
        <h1 className="text-3xl font-bold text-black">GRAMASSIST</h1>
      </div>

      {/* Chat Box */}
      <div className="w-full max-w-2xl bg-[#f4d37d] rounded-2xl p-4 flex flex-col justify-between h-[70vh] shadow-lg">
        <div className="flex-1 overflow-y-auto space-y-3">
          <AnimatePresence>
          {messages.map((msg, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -10 }}
              transition={{ duration: 0.3 }}
              className={`flex ${
                msg.role === "user" ? "justify-end" : "justify-start"
              }`}
            >
              <div
                className={`px-4 py-2 rounded-2xl max-w-xs ${
                  msg.role === "user"
                    ? "bg-[#a87000] text-white rounded-br-none"
                    : "bg-white text-gray-800 rounded-bl-none shadow"
                }`}
              >
                {msg.text}
              </div>
            </motion.div>
          ))}
          </AnimatePresence>
          {loading && (
            <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="text-gray-600 animate-pulse">Thinking...</motion.div>
          )}
        </div>

        {/* Input Area */}
        <div className="mt-4 flex bg-white rounded-full overflow-hidden shadow-md">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask me anything about GSU..."
            className="flex-1 px-4 py-2 focus:outline-none"
          />
          <button
            onClick={sendMessage}
            disabled={loading}
            className="bg-[#a87000] text-white px-6 font-semibold hover:bg-[#8c5f00] transition"
          >
            ➤
          </button>
        </div>
      </div>
    </div>
  );

};