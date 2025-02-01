function Item({ name, isPacked }) {
  return (
    <li className="item">
      {/* 나는 여기서 삼항연산자를 사용하지 않고 */}
      {/* return 이전에 새로운 변수를 생성해서 해결하였음 */}
      {/* 이런 방식이 더 직관적이고 새롭다. */}
      {name} {isPacked ? '✅' : '❌'}
    </li>
  );
}

export default function PackingList() {
  return (
    <section>
      <h1>Sally Ride's Packing List</h1>
      <ul>
        <Item
          isPacked={true}
          name="Space suit"
        />
        <Item
          isPacked={true}
          name="Helmet with a golden leaf"
        />
        <Item
          isPacked={false}
          name="Photo of Tam"
        />
      </ul>
    </section>
  );
}
