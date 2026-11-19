# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 325 (printed ٣٢٤)."""

PAGE_NUMBER = 325
PRINTED_PAGE = "٣٢٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # The matn «(التوابع)» on PDF p. 324 continues here with its predicate «(كل ثان)».
    {"type": "matn",
     "ar": "(كل ثان) أي: متأخر متى لوحظ مع سابقه[[١]] كان في الرتبة الثانية منه، فدخل فيه التابع الثاني والثالث فصاعدا",
     "en": "…(are every second [element]), that is, every later element which, whenever it is considered together with what precedes it, stands in the second rank relative to it; so the second, third and further appositives fall under it,"},
    {"type": "matn",
     "ar": "متلبس (بإعراب سابقه) أي: بجنس إعراب سابقه بحيث يكون إعرابه من جنس إعراب سابقه[[٢]] ناش كلاهما (من جهة[[٣]] واحدة) شخصية[[٤]]",
     "en": "bearing (the inflection of what precedes it), that is, the genus of the inflection of what precedes it, such that its inflection is of the genus of its antecedent’s inflection, both arising (from one [single] aspect), one individual aspect,"},
    {"type": "matn",
     "ar": "مثل: «جاءني زيد العالم»، فإن «العالم» إذا لوحظ مع «زيد» كان في الرتبة الثانية منه، وإعرابه من جنس إعرابه، وهو الرفع،",
     "en": "as in “Zayd the learned came to me”: when “the learned” is considered with “Zayd,” it stands in the second rank relative to it, and its inflection is of the genus of its inflection, namely the nominative;"},
    {"type": "matn",
     "ar": "والرفع في كل منهما ناش من جهة واحدة شخصية[[٥]]، هي فاعلية زيد العالم؛",
     "en": "and the nominative in each of them arises from one individual aspect, namely the agency of “Zayd the learned,”"},
    {"type": "matn",
     "ar": "لأن المجيء المنسوب[[٦]] إلى «زيد» في قصد المتكلم منسوب إليه مع تابعه لا إليه مطلقا.",
     "en": "because the coming attributed to “Zayd” is, in the speaker’s intent, attributed to him together with his appositive, not to him absolutely."},
    {"type": "matn",
     "ar": "فقوله: «كل ثان» يشمل التوابع، وخبر المبتدأ، وخبري «كان وإن»، وأخواتهما، وثاني مفعولي «ظننت وأعطيت».",
     "en": "His words “every second [element]” cover the appositives, the predicate of the mubtadaʾ, the two predicates of “kāna” and “inna” and their sisters, and the second object of “ẓanantu” and “aʿṭaytu.”"},
    {"type": "matn",
     "ar": "وقوله: «بإعراب سابقه» يخرج الكل إلا خبر المبتدأ وثاني مفعولي «ظننت وأعطيت».",
     "en": "His words “with the inflection of what precedes it” exclude all of these except the predicate of the mubtadaʾ and the second object of “ẓanantu” and “aʿṭaytu.”"},
    {"type": "matn",
     "ar": "وقوله: «من جهة واحدة» يخرج هذه الأشياء؛ لأن العامل في المبتدأ والخبر وإن كان هو الابتداء، أعني: التجريد عن العوامل اللفظية للإسناد،",
     "en": "His words “from one aspect” exclude these: for though the governor of the mubtadaʾ and the khabar is inception (al-ibtidāʾ), I mean being stripped of overt governors for the sake of predication,"},
    {"type": "matn",
     "ar": "لكن هذا المعنى من حيث إنه يقتضي مسندا إليه صار عاملا في الخبر، فليس ارتفاعهما من جهة واحدة،",
     "en": "yet this notion, in that it requires a subject, became the governor of the predicate; so their nominative does not arise from one aspect."},
    {"type": "matn",
     "ar": "وكذا «ظننت» من حيث إنه يقتضي مظنونا فيه ومظنونا عمل في مفعوليه، فليس انتصابهما من جهة واحدة.",
     "en": "Likewise “ẓanantu,” in that it requires something about which a supposition is made and something supposed, governs its two objects; so their accusative does not arise from one aspect."},
    {"type": "matn",
     "ar": "وكذلك «أعطيت» من حيث إنه يقتضي آخذا ومأخوذا عمل في مفعوليه، فليس انتصابهما من جهة واحدة.",
     "en": "Likewise “aʿṭaytu,” in that it requires a taker and a thing taken, governs its two objects; so their accusative does not arise from one aspect."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الذي هو متبوعه كان في الرتبة الثانية منه وإن كان في الرتبة الثالثة أو الرابعة مثلا بالقياس إلى غيره كالصفة الثالثة والرابعة،",
     "en": "[Its antecedent,] which is what it follows: it stands in the second rank relative to it, even if it stands in the third or fourth rank, for example, relative to something else, like the third and fourth adjective;"},
    {"type": "pair",
     "ar": "فقوله: ثان لبيان الحال لا للتصيير.",
     "en": "so his word “second” describes the state; it is not [a term] for making [something second]."},
    {"type": "pair",
     "ar": "ومنهم من قال: إن المراد بالثاني هو المتأخر مطلقا. وفيه ارتكاب عموم مجاز، وهو خلاف الأصل.",
     "en": "Some said: what is meant by “second” is what comes later absolutely. This involves a generalized figurative use (ʿumūm al-majāz), which is contrary to the default."},
    {"type": "pair",
     "ar": "وعلى القولين: لا يصدق التعريف على المعطوف المقدم على المعطوف عليه، مثل: عليك ورحمة الله السلام",
     "en": "On both views the definition does not apply to a conjoined noun placed before what it is conjoined to, as in “ʿalayka wa-raḥmatu Allāhi al-salāmu” (upon you, and the mercy of Allah, be peace),"},
    {"type": "pair",
     "ar": "إلا أن يراد السبق، والتأخر بحسب الرتبة.",
     "en": "unless precedence and posteriority are meant with respect to rank."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "مع أنهما متغايران شخصا بحسب القصد، فلا يرد النقض بقراءة الكتاب جزءا جزءا؛",
     "en": "Although the two differ individually in intent; so no objection arises from “reading the book part [by] part” (juzʾan juzʾan),"},
    {"type": "pair",
     "ar": "لأن إعرابهما واحد بحسب القصد، وظهر في موضعين.",
     "en": "since the inflection of the two is one in intent, appearing in two places."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: المقتضي للإعراب.",
     "en": "That is, what requires the inflection."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فلا يرد المفعول الثاني من باب «علمت» مثلا؛ إذ جهة نصبهما متحدة نوعا لا شخصا.",
     "en": "So the second object of the class of “ʿalimtu,” for example, is no objection, since the aspect of their accusative is one in kind, not individually."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وإن كان لغيرها مدخل في ذلك، وهو كونه نعتا للفاعل.",
     "en": "Even if something else plays a part in that, namely its being an attribute (naʿt) of the agent."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لأحد أن يناقش فيه بأنه يلزم أن يكون المقتضي لإعراب «زيد» في «جاءني غلام زيد» هو فاعلية «غلام زيد»؛",
     "en": "One may dispute this: it would follow that what requires the inflection of “Zayd” in “Zayd’s slave came to me” is the agency of “Zayd’s slave,”"},
    # REVIEW: print reads «المجيء المنصوب إلى غلام»; the matn has «المنسوب»; transcribed as printed.
    {"type": "pair",
     "ar": "لأن المجيء المنصوب إلى غلام في قصد المتكلم منسوب إليه مع \"زيد\" لا إليه مطلقا.",
     "en": "since the coming attributed [printed: “manṣūb”] to “slave” is, in the speaker’s intent, attributed to it together with “Zayd,” not to it absolutely."},
    {"type": "pair",
     "ar": "اللهم إلا أن يراد المعية في الانتساب إليه؛ لأن النعت هو المنعوت بحسب الذات.",
     "en": "Unless, that is, togetherness in the attribution to it is meant; for the attribute is the thing qualified in its essence."},
]
