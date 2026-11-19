# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 82 (printed ٨١)."""

PAGE_NUMBER = 82
PRINTED_PAGE = "٨١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "(و) كما في الاسم المعرب بالحركة، المضافة إلى ياء المتكلم، نحو: (غلامي[[١]])،",
     "en": "(And) as in the noun inflected by vowel that is annexed to the yāʾ of the speaker (yāʾ al-mutakallim), for example (ghulāmī [my boy])."},
    {"type": "matn",
     "ar": "فإنه لما اشتغل ما قبل ياء المتكلم بالكسرة للمناسبة قبل دخول العامل، امتنع أن يدخل عليه حركة أخرى، حالة دخوله بعد دخوله، موافقة لها، أو مخالفة.",
     "en": "For since what precedes the yāʾ of the speaker is occupied with a kasra for the sake of concord — before the entry of the governing operator (ʿāmil) — it is precluded that another vowel should come upon it at the moment of [the operator’s] entry, after [the kasra’s] entry, whether agreeing with it or differing from it."},
    {"type": "matn",
     "ar": "فما ذهب إليه بعض من أن إعراب مثل هذا الاسم في حالة الجر لفظي غير مرضي.",
     "en": "So what some have held — that the inflection of such a noun in the state of the genitive is pronounced (lafẓī) — is not satisfactory."},
    {"type": "matn",
     "ar": "(مطلقا) أي: في الأحوال الثلاث، يعني: كون الإعراب تقديريا في هذين النوعين من الاسم المعرب، إنما هو في جميع الأحوال غير مختص ببعضها.",
     "en": "(Absolutely [muṭlaqan]) — that is: in [all] three states — meaning that the inflection’s being estimated in these two kinds of declinable noun obtains in all states, not restricted to some of them."},
    {"type": "matn",
     "ar": "(أو استثقل) عطف على قوله: «تعذر»، أي: تقدير الإعراب فيما تعذر، أو في الاسم الذي استثقل ظهور الإعراب في لفظه[[٢]]، وذلك إذا كان محل الإعراب قابلا للحركة الإعرابية، ولكن يكون بظهوره[[٣]] في اللفظ ثقيلا على اللسان،",
     "en": "(Or it is found burdensome [ustuthqila]) — coordinated with his words “is precluded” — that is: the estimation of inflection in that in which it is precluded, or in the noun in whose wording the manifestation of inflection is found burdensome; and that is when the locus of inflection is receptive to the inflectional vowel, but its manifestation in the utterance would be heavy upon the tongue,"},
    {"type": "matn",
     "ar": "كما في الاسم الذي في آخره ياء مكسور ما قبلها، سواء كانت محذوفة بالتقاء الساكنين (كقاض) أو غير محذوفة كـ«القاضي» (رفعا وجرا)[[٤]] أي: في حالتي الرفع والجر، لا في حالة النصب، لاستثقال الضمة والكسرة على الياء[[٥]] دون الفتحة.",
     "en": "as in the noun at whose end is a yāʾ preceded by a kasra — whether elided through the meeting of two quiescents (as in “qāḍin”) or not elided (as in “al-qāḍī”) — (in the nominative and the genitive) — that is: in the two states of nominative and genitive, not in the state of the accusative, because of the burdensomeness of the ḍamma and the kasra upon the yāʾ, as opposed to the fatḥa."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "خبر مبتدأ محذوف، والتقدير: هو، أي: ما تعذر عصا وغلامي وأمثاله، أو صفة مصدر محذوف، أي: تعذرا كتعذر عصا وغلامي.",
     "en": "[It is] the predicate of an omitted subject (mubtadaʾ), the implied [subject] being “it” — that is, “that in which [inflection] is precluded,” [namely] “ʿaṣā,” “ghulāmī,” and the like; or [it is] the qualifier of an omitted verbal noun, i.e., “a preclusion like the preclusion of ʿaṣā and ghulāmī.”"},
    {"type": "pair",
     "ar": "وإن جعلت الكاف اسمية جاز أن يكون كعصا وغلامي بدلا من قوله: ما تعذر، أو بيانا له.",
     "en": "And if you take the kāf [of comparison] to be nominal, it is permissible for “ka-ʿaṣā wa-ghulāmī” to be a substitute (badal) for his words “that in which it is precluded,” or an explication of it."},
    {"type": "pair",
     "ar": "وقوله: «مطلقا» على التقدير الأول حال من مدخول الكاف، والعامل فيه ما يتضمنه الكاف من معنى التمثيل، أو ما يفهم من الكلام من التعذر، أو تقدير الإعراب،",
     "en": "As for his words “muṭlaqan” (absolutely): on the first estimation it is a circumstantial qualifier (ḥāl) of the object of the kāf, the operator governing it being the sense of exemplification contained in the kāf, or what is understood from the discourse — [namely] preclusion, or the estimation of inflection;"},
    {"type": "pair",
     "ar": "وعلى التقدير الثاني حال مما أضيف إليه التعذر المحذوف، أو ظرف، أو مصدر لذلك المحذوف. والمعنى: كتعذره في زمان مطلق، أو تعذرا مطلقا،",
     "en": "and on the second estimation it is a ḥāl of that to which the omitted “preclusion” is annexed, or an adverbial [of time], or a verbal noun for that omitted [term] — the meaning being “like its preclusion in an unrestricted time,” or “an unrestricted preclusion”;"},
    {"type": "pair",
     "ar": "وعلى التقدير الثالث حال من قوله: كعصا وغلامي، والعامل فيه ما هو عامل في الظرف المستقر، أو ظرف لذلك العامل.",
     "en": "and on the third estimation it is a ḥāl of his words “ka-ʿaṣā wa-ghulāmī,” the operator governing it being that which governs [it] within the implicit adverbial container (al-ẓarf al-mustaqarr), or an adverbial for that operator."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: لفظ الاسم المعرب.",
     "en": "That is: the wording of the declinable noun."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: ظهور الإعراب.",
     "en": "That is: the manifestation of inflection."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يعني: أن «رفعا وجرا» ظرف للاستثقال المقدر، والمعنى كاستثقال قاض استثقالا وقت مرفوعيته ومجروريته، أو وقت رفع العامل وجره له.",
     "en": "He means that “rafʿan wa jarran” (nominative and genitive) is an adverbial container (ẓarf) for the estimated burdening (istithqāl), the sense being: “like the burdening of ‘qāḍin’ — a burdening at the time of its being nominative and its being genitive,” or “at the time of the operator’s making it nominative and genitive.”"},
    {"type": "pair",
     "ar": "ولك أن تجعله مصدرا، أي: استثقال رفع وجر، وحالا مما أضيف إليه الاستثقال المقدر، أي: حال كونه مرفوعا ومجرورا، إلى غير ذلك من الاحتمالات التي ذكرناها في قوله: «مطلقا».",
     "en": "You may also take it as a verbal noun, i.e., “the burdening of a nominative and a genitive,” and as a ḥāl of that to which the estimated “burdening” is annexed, i.e., “in the state of its being nominative and genitive” — along with the other possibilities that we mentioned regarding his words “muṭlaqan.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "المكسورة ما قبلها. قال الشيخ الرضي: وذلك محسوس لضعف الياء، وثقل الحركتين مع تحرك ما قبلها بحركة ثقيلة، فإن سكن ما قبلها لم تستثقل الحركتان كظبي وكرسي.",
     "en": "[The yāʾ] whose preceding [letter] bears a kasra. Shaykh al-Raḍī said: This is perceptible [to the senses], on account of the weakness of the yāʾ and the heaviness of the two vowels together with the preceding letter’s being voweled with a heavy vowel [the kasra]. But if what precedes it is quiescent, the two vowels are not found burdensome, as in “ẓaby” and “kursī.”"},
]
