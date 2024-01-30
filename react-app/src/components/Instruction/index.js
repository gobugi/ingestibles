import { React } from "react";
import "./Instruction.css"

const Instruction = (instruction) => {
  return(
    <div id="step-details">
      {instruction.instruction.imageUrl && instruction.instruction.imageUrl !== 'null' && instruction.instruction.imageUrl !== 'undefined' && <img src={instruction.instruction.imageUrl} alt="step"/>}
      <br/><br/>
      <p id="step-directions">{instruction.instruction.directions}</p>
      <div id="comment-button-container">
        <a href="#comments-section" id="comment-button"><i className="fas fa-comments" id="icon"></i>Comment</a>
      </div>
    </div>
  )
}


export default Instruction
