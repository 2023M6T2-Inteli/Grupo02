import Teste2 from "@/components/componente";
//import tailwind

var a = [
  { name: "alberto", idade: "21", fact: "muito legal" },
  { name: "tainara", idade: "20", fact: "gosto moda" },
  { name: "amanda", idade: "20", fact: "gosta de dançar" },
];
function Teste() {
  return (
    <div>
      {a.map((item) => {
        return (
          <Teste2
            name={item.name}
            fact={item.fact}
            idade={item.idade}
            key={item.name}
          ></Teste2>
        );
      })}
      <p className="text-red-600 ">aaa</p>
    </div>
  );
}

export default Teste;
