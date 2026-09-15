// Lesson 11 — Hard P03: Multi-language app with Context
import { createContext, useContext, useState, useCallback } from "react";
const translations = {
  en: { welcome: "Welcome", goodbye: "Goodbye", settings: "Settings", profile: "Profile", logout: "Logout" },
  es: { welcome: "Bienvenido", goodbye: "Adiós", settings: "Configuración", profile: "Perfil", logout: "Cerrar sesión" },
  fr: { welcome: "Bienvenue", goodbye: "Au revoir", settings: "Paramètres", profile: "Profil", logout: "Déconnexion" },
};
const LanguageContext = createContext(null);
function useTranslation() {
  const { lang } = useContext(LanguageContext);
  const t = useCallback((key) => translations[lang]?.[key] || key, [lang]);
  return { t, lang };
}
function LanguageProvider({ children }) {
  const [lang, setLang] = useState("en");
  return <LanguageContext.Provider value={{ lang, setLang }}>{children}</LanguageContext.Provider>;
}
function App() {
  const { t, lang } = useTranslation();
  const { setLang } = useContext(LanguageContext);
  return (
    <LanguageProvider>
      <div>
        <h1>{t("welcome")}</h1>
        <p>{t("settings")} | {t("profile")} | {t("logout")}</p>
        <button onClick={() => setLang("en")}>EN</button>
        <button onClick={() => setLang("es")}>ES</button>
        <button onClick={() => setLang("fr")}>FR</button>
      </div>
    </LanguageProvider>
  );
}
export default App;
