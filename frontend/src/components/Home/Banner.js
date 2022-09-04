import React, { useState } from "react";
import logo from "../../imgs/logo.png";
import agent from "../../agent";
import { connect } from "react-redux";
import { SEARCH_BY_TITLE } from "../../constants/actionTypes";

const mapDispatchToProps = (dispatch) => ({
  search: (term) =>
    dispatch({
      type: SEARCH_BY_TITLE,
      payload: agent.Items.byTitle(term, 1),
      searchTerm: term,
      searchTriggered: true,
    }),
});

const Banner = (props) => {
  const [showSearch, setShowSearch] = useState(false);

  const handleChange = (ev) => {
    ev.preventDefault();
    console.log(ev.target.value);
    if (ev.target.value.length >= 3) {
      props.search(ev.target.value);
    } else if (ev.target.value.length == 0) {
      props.search("");
    }
  };

  return (
    <div className="banner text-white">
      <div className="container p-4 text-center">
        <img src={logo} alt="banner" />
        <div className="searchCover">
          <span id="get-part">
            A place to{" "}
            <span
              onClick={() => {
                setShowSearch(true);
              }}
            >
              get
            </span>
          </span>
          {showSearch && (
            <span>
              <span>
                <input
                  id="search-box"
                  placeholder="What is it that you truly desire?"
                  className="searchBox m-2"
                  onChange={handleChange}
                ></input>
                <img
                  className="magImage"
                  height="25px"
                  width="25px"
                  src="https://static.thenounproject.com/png/101791-200.png"
                />
              </span>
              <span className="coolStuff"> the cool stuff.</span>
            </span>
          )}
          {!showSearch && <span> the cool stuff.</span>}
        </div>
      </div>
    </div>
  );
};

export default connect(() => ({}), mapDispatchToProps)(Banner);
