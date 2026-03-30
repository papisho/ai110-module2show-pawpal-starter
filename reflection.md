# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

### Core User Actions
1. Register an owner and their pet — The user enters basic 
   information (owner name, pet name, species) to set up 
   their profile in the app.

2. Add and manage daily care tasks — The user creates tasks 
   (e.g., morning walk, feeding, medication) with a duration 
   in minutes and a priority level (low, medium, high).

3. Generate and view a daily schedule — The user triggers the 
   scheduler to produce an ordered daily care plan, including 
   a brief explanation of why each task was selected and when 
   it happens.

### Classes and Responsibilities
- **Owner** — holds the owner's name and a list of their pets.
  Responsible for managing pet registration.

- **Pet** — holds the pet's name, species, age, and task list.
  Responsible for managing its own care tasks.

- **Task** — holds a single care task's details (title, duration,
  priority, recurring flag). Responsible for representing one
  unit of pet care.

- **Scheduler** — holds a reference to a Pet and builds a daily
  schedule from its tasks. Responsible for sorting, conflict
  detection, and explaining the plan.

**b. Design changes**
After asking Copilot to review the skeleton, it flagged six issues.
I made the following changes:

1. Replaced priority str with a Priority Enum — prevents typos like
   "High" or "urgent" from silently breaking sort logic.

2. Added time_of_day field to Task — enables basic conflict detection
   (e.g. two "morning" tasks that overlap).

3. Added __post_init__ validation to Task and Pet — catches invalid
   values like negative age or zero-duration tasks early.

4. Changed get_tasks() and get_pets() to return copies — prevents
   external code from accidentally mutating internal state.

I skipped the ScheduledTask suggestion for now because it adds
complexity before the core logic is implemented. I will revisit
it in Phase 3 if explain_plan() needs richer output.


## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
