# -*- coding: utf-8 -*-
"""
Mulla Jami — al-Fawa'id al-Diya'iyya (commentary on al-Kafiya of Ibn al-Hajib)
Source page: 27 of the PDF  (printed page ٢٦) — continuation of the Introduction.

Block types:
  khutba – the opening authorial address (matn), ar + en
  matn   – a sentence of the base text (matn), ar + en
  note   – opens a numbered footnote (num + optional label)
  pair   – a sentence pair inside the current footnote, ar + en
  rule   – a decorative divider
"""

PAGE_NUMBER = 27          # PDF page
PRINTED_PAGE = "٢٦"       # page number printed in the book

BLOCKS = [
    # ---------------- The base text (matn / khutba) ----------------
    {"type": "khutba",
     "ar": "الضيائية[[١]]»؛ لأنه لهذا الجمع والتأليف[[٢]] كالعلة الغائية[[٣]]،",
     "en": "al-Ḍiyāʾiyya”; for he is, in relation to this compilation and composition, like the final cause,"},
    {"type": "khutba",
     "ar": "نفعه[[٤]] الله تعالى بها[[٥]] وسائر[[٦]] المبتدئين من أصحاب التحصيل[[٧]]،",
     "en": "—may God the Exalted benefit him by them, and [likewise] the rest of the beginners among the seekers of learning—"},
    {"type": "khutba",
     "ar": "وما توفيقي إلا بالله[[٨]]، ......",
     "en": "and my success is only through God, ......"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فإن قلت: قد تقرر في محله أن النسبة إلى ابن الزبير «زبيري»، فكيف جعلت النسبة إلى ضياء الدين ضيائية؟",
     "en": "If you should say: it is established in its proper place that the relative adjective (nisba) from “Ibn al-Zubayr” is “Zubayrī” — so how was the nisba from “Ḍiyāʾ al-Dīn” made “Ḍiyāʾiyya”?"},
    {"type": "pair",
     "ar": "قلت: مبنى النسبة في التركيب الإضافي الجزء الثاني إن كان مقصودا في التركيب الإضافي.",
     "en": "I say: the basis of the nisba in a genitive construction is the second element, if it is what is intended in the genitive construction."},
    {"type": "pair",
     "ar": "وإن لم يكن مقصودا فيه فبالنسبة إلى الجزء الأول.",
     "en": "But if it is not what is intended therein, then [the nisba] is formed from the first element."},
    {"type": "pair",
     "ar": "والمقصود في «ضياء الدين» الجزء الأول ليجعل الشخص ضياء للدين،",
     "en": "In “Ḍiyāʾ al-Dīn” what is intended is the first element, so as to render the person a “light (ḍiyāʾ) of the religion,”"},
    {"type": "pair",
     "ar": "والمقصود في «ابن الزبير» الزبير ليرتفع قدر الشخص بالنسبة إلى الزبير، بخلاف عبد مناف،",
     "en": "whereas in “Ibn al-Zubayr” what is intended is “al-Zubayr,” so that the person’s rank is raised by ascription to al-Zubayr — unlike “ʿAbd Manāf,”"},
    {"type": "pair",
     "ar": "فإن المقصود إظهار كماله في العبودية، حتى خص من بين عباد المضاف إليه باسم العبد، كأنه العبد.",
     "en": "for [there] the intent is to display his perfection in servitude, so that from among the servants of the one to whom [the name] is annexed he alone was designated by the name “the servant,” as though he were the [sole] servant."},
    {"type": "pair",
     "ar": "فإن قلت: لم لم ينسبه إلى اسمه، مع أن النسبة إليه خالية من تكلف الحذف؟",
     "en": "If you should say: why did he not form the nisba from his given name, seeing that a nisba from it would be free of the artificiality of ellipsis?"},
    {"type": "pair",
     "ar": "قلت: لأن المنسوب إليه اشتهر باللقب، ولأن في اللقب ما يمدحه ويجعله حقيقا بأن يجعل علة غائية للتأليف،",
     "en": "I say: because the one so ascribed became renowned by his title (laqab); and because the title contains that which praises him and renders him worthy of being made the final cause of the composition;"},
    {"type": "pair",
     "ar": "ولأن فيه نسبة إلى الضياء بحسب أصل المعنى، فيشعر بأنه يضيء القلوب، ويزيل عنها ظلمة الريب.",
     "en": "and because it involves an ascription to “light” (ḍiyāʾ) according to the original meaning, so it intimates that he illumines hearts and dispels from them the darkness of doubts (riyab)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الأولى ترك الجمع؛ لأنه لا فائدة فيه إلا إخراج الفقرتين عن المساواة.",
     "en": "It would have been preferable to omit the coordination [“and composition”], since it serves no purpose except to remove the two clauses from [rhythmic] parity."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فاعلم أن العلل أربع عندهم:",
     "en": "Know that the causes, in their [the philosophers’] view, are four:"},
    {"type": "pair",
     "ar": "العلة الفاعلية: وهي مؤلف هذا الكتاب.",
     "en": "the efficient cause (al-ʿilla al-fāʿiliyya), which is the author of this book;"},
    {"type": "pair",
     "ar": "والعلة المادية: وهي الألفاظ وكلمات الكتاب.",
     "en": "the material cause (al-ʿilla al-māddiyya), which is the wording and words of the book;"},
    {"type": "pair",
     "ar": "والعلة الصورية: جرم هذا الكتاب.",
     "en": "the formal cause (al-ʿilla al-ṣūriyya), which is the physical body of this book;"},
    {"type": "pair",
     "ar": "والعلة الغائية: ما تقدم في التصور وتأخر في الوجود.",
     "en": "and the final cause (al-ʿilla al-ghāʾiyya): that which is prior in conception yet posterior in existence."},
    {"type": "pair",
     "ar": "وضياء الدين يوسف متقدم في التصور، لكن لم يتأخر في الوجود، والعلة الغائية تعلمه هذا الشرح.",
     "en": "Now Ḍiyāʾ al-Dīn Yūsuf is prior in conception, yet he is not posterior in existence; [rather] the [true] final cause is his learning this commentary."},
    {"type": "pair",
     "ar": "ولو قال: لأن تعلمه العلة الغائية، لصح واتضح وكفى في النسبة.",
     "en": "Had he said, “because his learning [it] is the final cause,” it would have been correct, clear, and sufficient with respect to the ascription."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: يوسف.",
     "en": "That is: Yūsuf."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: بالضيائية.",
     "en": "That is: by [the notes named] al-Ḍiyāʾiyya."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "بالنصب عطف على ضمير «نفعه». والسائر من السؤر بمعنى الباقي.",
     "en": "In the accusative, coordinated with the pronominal object of “nafaʿahu” (may He benefit him). “Al-sāʾir” derives from “al-suʾr,” meaning the remainder/rest."},
    {"type": "pair",
     "ar": "وقيل: وقد يستعمل بمعنى الجميع، وهو في كلام المصنفين كالزمخشري. وقد أثبته في القاموس على قلة.",
     "en": "It is said: it is sometimes used in the sense of “the whole,” as occurs in the writings of authors such as al-Zamakhsharī; and [the author of] al-Qāmūs recorded this [usage], [noting it to be] rare."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: من المتعلمين؛ لأن التحصيل خاص في العرف بتحصيل العلم، وهذا احتراز من أهل الصنائع والحرف.",
     "en": "That is: among the learners; because “taḥṣīl” is, by convention, restricted to the acquisition of knowledge — this being a precaution to exclude the people of crafts and trades."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "التوفيق: جعل الأسباب موافقة للمطلوب.",
     "en": "“Al-tawfīq” (divinely granted success) is the making of the means conformable to what is sought."},
    {"type": "pair",
     "ar": "قال عبد الحكيم: ويشترط أن يكون المطلوب خيرا، فإنه إذا كان شرا يقال له: الخذلان.",
     "en": "ʿAbd al-Ḥakīm said: it is stipulated that what is sought be good; for if it is evil it is called “khidhlān” (abandonment)."},
    {"type": "pair",
     "ar": "قال عصمت: قوله: «وما توفيقي إلا بالله» لما أسند هذا النظم اللطيف والتأليف الشريف إلى نفسه، قال: وما توفيقي إلا بالله، دفعا لتوهم ادعاء الاستقلال.",
     "en": "ʿIṣmat said: as for his words “and my success is only through God” — when he attributed this fine arrangement and noble composition to himself, he said “and my success is only through God” in order to ward off the false impression of a claim to independence [from God]."},
    {"type": "pair",
     "ar": "والتوفيق: جعل الأسباب موافقة لمسبباتها. والمراد: أن يكون أسباب حصول هذا التأليف موافقة له ليس إلا بالله تعالى.",
     "en": "“Al-tawfīq” is the making of the causes conformable to their effects; and what is meant is that the means for the accomplishment of this composition being made conformable to it comes only through God, the Exalted."},
    {"type": "pair",
     "ar": "قيل: لا بد من تقييد مفهوم التوفيق بما يخصه بالخير، فإن جعل أسباب الشر موافقا له لا يسمى توفيقا.",
     "en": "It is said: the concept of tawfīq must be qualified by that which restricts it to the good, for making the causes of evil conformable to it is not called “tawfīq.”"},
    {"type": "pair",
     "ar": "ثم لا يخفى أن فاعل التوفيق هو الله سبحانه. ومن قاعدتهم: أنه لا ينسب الفعل إلى فاعله بالباء،",
     "en": "Furthermore, it is evident that the agent of tawfīq is God, Glorified is He. Now, among their [the grammarians’] rules is that an act is not ascribed to its agent by means of the preposition bi- —"},
]
