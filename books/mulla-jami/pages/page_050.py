# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 50 (printed ٤٩)."""

PAGE_NUMBER = 50
PRINTED_PAGE = "٤٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "وفي بعض الحواشي[[١]]: أن المراد بالإسناد: هو الإسناد المقصود لذاته، وحينئذ يكون الكلام عند المصنف أيضا أخص[[٢]] من الجملة.",
     "en": "And in some of the glosses [it is stated]: that what is meant by “predication” is the predication intended for its own sake; and in that case “speech” according to the author too is more specific than “sentence.”"},
    {"type": "matn",
     "ar": "(ولا يتأتى) أي: لا يحصل (ذلك) أي: الكلام[[٣]] (إلا في) ضمن (اسمين).",
     "en": "His words “and it does not come about (wa-lā yataʾattā)” mean: it is not realized; “that (dhālika)” means: speech; “except in (illā fī),” i.e. within, “two nouns (ismayn).”"},
    {"type": "matn",
     "ar": "أحدهما: مسند.",
     "en": "one of them being a predicate (musnad),"},
    {"type": "matn",
     "ar": "والآخر: مسند إليه. (أو في) ضمن (اسم) مسند إليه (وفعل) مسند.",
     "en": "and the other a subject (musnad ilayhi); “or in (aw fī),” i.e. within, “a noun (ism)” [as] subject “and a verb (wa-fiʿl)” [as] predicate."},
    {"type": "matn",
     "ar": "وفي بعض النسخ: «أو في فعل واسم».",
     "en": "And in some copies [it reads]: “or in a verb and a noun.”"},
    {"type": "matn",
     "ar": "فإن التركيب الثنائي العقلي بين الأقسام الثلاثة يرتقي إلى ستة أقسام:",
     "en": "For the rational binary combination among the three categories rises to six divisions:"},
    {"type": "matn",
     "ar": "ثلاثة منها: من جنس واحد: اسم واسم، فعل وفعل، حرف وحرف.",
     "en": "three of them of a single genus: noun and noun, verb and verb, particle and particle;"},
    {"type": "matn",
     "ar": "وثلاثة منها من جنسين: اسم وفعل، اسم وحرف، فعل وحرف.",
     "en": "and three of them of two genera: noun and verb, noun and particle, verb and particle."},
    {"type": "matn",
     "ar": "ومن البين: أن الكلام لا يحصل بدون الإسناد، ولا بد له من مسند ومسند إليه، وهما لا يتحققان إلا في اسمين، أو في اسم وفعل.",
     "en": "It is evident that speech is not realized without predication, and it must have a predicate and a subject, and these two are realized only in two nouns, or in a noun and a verb."},
    {"type": "matn",
     "ar": "وأما الأقسام الأربعة الباقية: ففي الحرف والحرف كلاهما مفقودان، وفي الفعل والفعل، والفعل والحرف المسند إليه مفقود، وفي الاسم والحرف أحدهما مفقود، فإن الاسم إن كان مسندا، فالمسند إليه مفقود، وإن كان مسندا إليه، فالمسند مفقود.",
     "en": "As for the four remaining divisions: in [the combination of] particle and particle, both [predicate and subject] are absent; in verb and verb, and in verb and particle, the subject is absent; and in noun and particle, one of the two is absent — for if the noun is a predicate, then the subject is absent, and if it is a subject, then the predicate is absent."},
    {"type": "matn",
     "ar": "ونحو: «يا زيد» بتقدير: «أدعو[[٤]] زيدا»[[٥]]، فلم يكن من تركيب الحرف والاسم، بل من تركيب الفعل والاسم، الذي هو المنوي[[٦]] في «أدعو».",
     "en": "And [an expression] such as “O Zayd (yā Zaydu)” — with the implied reconstruction “I call Zayd (adʿū Zaydan)” — is not of the composition of particle and noun, but rather of the composition of verb and noun, [the noun] being that which is intended implicitly (al-manwī) in “adʿū.”"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: المنسوبة إلى المصنف، فإنه كتب حواشي على هامش الكتاب حال المذاكرة، أو الحواشي التي كتبها التلامذة بإملائه، وهي المسماة بـ«الأمالي»، غير الإيضاح شرح الكتاب.",
     "en": "That is: those [glosses] attributed to the author, for he wrote glosses in the margin of the book during study-discussion (mudhākara); or the glosses that the students wrote at his dictation, which are the ones named “al-Amālī,” as distinct from al-Īḍāḥ, [namely] Sharḥ al-Kitāb."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ويقال: إن قول المصنف في بحث حروف الاستفهام: إن لها صدر الكلام ينافي هذا المرام.",
     "en": "It may be said: that the author’s statement in the discussion of the interrogative particles — namely, that they [take] the beginning of the speech (ṣadr al-kalām) — contradicts this aim."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أشار بذلك إلى الكلام لا إلى تعريفه، أو التضمن، أو الإسناد؛ لأن الكلام مسوق للكلام ولبعده، ولأن قوله: «ولا يأتي» إشارة إلى تقسيم الكلام بعد تعريفه.",
     "en": "By “that (dhālika)” he pointed to “speech,” not to its definition, nor to “comprising (taḍammun),” nor to “predication” — because the discourse is set forth for [the sake of] speech, and because of the remoteness [of the other referents]; and because his words “and it does not come (wa-lā yaʾtī)” are an indication of the division of speech after its definition."},
    {"type": "pair",
     "ar": "كما أن قوله: «وهي: اسم وفعل وحرف» تقسيم للكلمة بعد تعريفها. وإنما صرح فيه بأداة الحصر للعناية بشأن الحصر؛ لأن التركيب العقلي من الاثنين يرتقي إلى ستة.",
     "en": "just as his words “and it [the word] is: noun, verb, and particle” are a division of the word (kalima) after its definition. He made the restrictive particle (adāt al-ḥaṣr) explicit in it only out of concern for the matter of restriction, because the rational combination of the two [elements] rises to six."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "المنقول إلى الإنشاء قبل التقديم أو بعده.",
     "en": "[It is] that which is transferred to the performative (inshāʾ), whether before the preposing (taqdīm) or after it."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "كما ذهب إليه المبرد. ولذا صرح المصنف بالحصر في تقسيم الكلام دون تقسيم الكلمة.",
     "en": "As al-Mubarrad held. For this reason the author made the restriction explicit in the division of speech, but not in the division of the word."},
    {"type": "pair",
     "ar": "وقيل: لأن تعريف الكلام يرشد إلى أقسام ستة بخلاف بادئ الرأي في تعريف الكلمة.",
     "en": "And it has been said: [this is] because the definition of speech guides to six divisions, unlike the first impression (bādiʾ al-raʾy) in the definition of the word."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: المقدر في «أدعو»، وهو أنا، فالمنادى ليس بجزء من الجملة.",
     "en": "That is: the one implicitly reconstructed in “adʿū,” namely “I (anā)”; so the one called (al-munādā) is not a part of the sentence."},
]
