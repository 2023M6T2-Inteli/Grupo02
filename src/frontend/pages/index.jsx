export default function Init() {
  return (

      <div className="w-screen h-screen bg-azul flex items-center flex-col justify-center gap-y-28">
        <div className="flex items-center flex-col justify-center gap-y-8">
          <img src="https://i.ibb.co/Fg0ZfTS/logo.png" className="w-44"/>

          <p> Bem-vindo de volta </p> 

        </div>
        <a href="/setup" className="bg-white px-7 py-4 rounded-full ">  
            Iniciar inspeção de espaços confinados 
        </a>

      </div>

  );
}