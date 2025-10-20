const quizArea = document.getElementById('quiz-area');
const progress = document.getElementById('progress-bar');
const total = quiz.questions.length;
const answered = new Set();

    // --- Render all questions ---
    quiz.questions.forEach((q, i) => {
      const block = document.createElement('div');
      block.classList.add('question-block');
      block.innerHTML = `
        <p style="padding: 0 100px"><b>Q${i + 1}:</b> ${q.question}</p>
        <div class="answers-row">
          ${q.answers.map(a => `
            <button type="button" class="answer-btn" 
                    data-qindex="${i}" data-value="${a}">
              ${a}
            </button>`).join('')}
        </div>
        <input type="hidden" name="answer_${i}" id="answer_${i}">
      `;
      quizArea.appendChild(block);
    });

    // --- Handle selection ---
    document.querySelectorAll('.answer-btn').forEach(btn => {
      btn.addEventListener('click', function () {
        const qidx = this.dataset.qindex;
        document.querySelectorAll(`.answer-btn[data-qindex="${qidx}"]`)
                .forEach(b => b.classList.remove('selected'));
        this.classList.add('selected');
        document.getElementById(`answer_${qidx}`).value = this.dataset.value;
        answered.add(qidx);
        progress.style.width = `${(answered.size / total) * 100}%`;
      });
    });