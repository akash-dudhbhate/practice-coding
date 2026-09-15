// Lesson 11 — Easy P03: Language Context
import { createContext, useContext, useState } from "react";
const LangContext = createContext("en");
const greetings = { en: "Hello", es: "Hola", fr: "Bonjour" };
function Greeting() {
  const lang = useContext(LangContext);
  return <p>{greetings[lang]}!</p>;
}
function App() {
  const [lang, setLang] = useState("en");
  return (
    <LangContext.Provider value={lang}>
      <Greeting />
      <button onClick={() => setLang("en")}>EN</button>
      <button onClick={() => setLang("es")}>ES</button>
      <button onClick={() => setLang("fr")}>FR</button>
    </LangContext.Provider>
  );
}
export default App;
