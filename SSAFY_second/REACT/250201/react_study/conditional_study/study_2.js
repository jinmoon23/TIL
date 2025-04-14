function Item({ name, importance }) {
  let decider = importance > 0 ? true : false
  return (
    <li className="item">
      {name} {decider ? <i>(importance: {importance})</i> : ''}
    </li>
  );
}

export default function PackingList() {
  return (
    <section>
      <h1>Sally Ride's Packing List</h1>
      <ul>
        <Item
          importance={9}
          name="Space suit"
        />
        <Item
          importance={0}
          name="Helmet with a golden leaf"
        />
        <Item
          importance={6}
          name="Photo of Tam"
        />
      </ul>
    </section>
  );
}
