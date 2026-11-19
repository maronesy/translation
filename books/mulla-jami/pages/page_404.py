# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 404 (printed ٤٠٣)."""

PAGE_NUMBER = 404
PRINTED_PAGE = "٤٠٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «بمعنى أنه تتأتى تلك الوجوه في جميع هذه الأسماء،» at the foot of PDF p. 403.
    {"type": "matn",
     "ar": "لا في كل واحد منها[[١]]، وهي: «من، وما، وأي، وأين، وأنى، ومتى» مشتركة بين الاستفهام والشرط، و«إذا» مختصة بالشرط، و«أيان وكيف» مختصتين بالاستفهام.",
     "en": "…not in each one of them. They are: “man” (who), “mā” (what), “ayy” (which), “ayna” (where), “annā” (whence, how) and “matā” (when), shared between interrogation and condition; “idhā” (when), restricted to condition; and “ayyāna” (when) and “kayfa” (how), restricted to interrogation."},
    # REVIEW: «مختصتين» printed (accusative/genitive form) where the parallel «مختصة» suggests «مختصتان»; transcribed as printed.
    {"type": "matn",
     "ar": "فـ«من وما» إذا كانتا استفهاميتين يتأتى فيهما الوجوه الثلاثة الأول، نحو: «من ضربت؟ وما صنعت؟ وبمن مررت؟ وغلام من ضربت؟ ومن ضربته؟ وما صنعته؟»،",
     "en": "So “man” and “mā”, when interrogative, admit the first three possibilities, as in “man ḍarabta?” (whom did you strike?), “mā ṣanaʿta?” (what did you do?), “bi-man mararta?” (by whom did you pass?), “ghulāma man ḍarabta?” (whose slave did you strike?), “man ḍarabtahu?” (who is it you struck?) and “mā ṣanaʿtahu?” (what is it you did?)."},
    {"type": "matn",
     "ar": "ولا يتأتى فيهما الرفع[[٢]] على الخبرية لامتناع ظرفيتهما،",
     "en": "The nominative as predicate is not available in them, since they cannot be adverbs."},
    {"type": "matn",
     "ar": "وإذا كانتا شرطيتين فكذلك يتأتى فيهما تلك الوجوه الثلاثة[[٣]]، نحو: «من تضرب أضرب، وما تصنع أصنع، وبمن تمرر أمرر، وغلام من تضرب أضربه، ومن يأتيني فهو مكرم»، ﴿وما تقدموا لأنفسكم من خير تجدوه عند الله﴾[[٤]].",
     "en": "When they are conditional, those three possibilities are likewise available in them, as in “man taḍrib aḍrib” (whomever you strike, I strike), “mā taṣnaʿ aṣnaʿ” (whatever you do, I do), “bi-man tamrur amrur” (by whomever you pass, I pass), “ghulāma man taḍrib aḍribhu” (whosever slave you strike, I strike him), “man yaʾtīnī fa-huwa mukram” (whoever comes to me is honoured), and “Whatever good you send ahead for yourselves, you will find it with Allah.”"},
    {"type": "matn",
     "ar": "ولا يتأتى فيهما -بل في جميع أسماء الشرط- الرفع على الخبرية، فإنه لا يقع بعدها إلا الفعل، ولا يصلح الفعل للابتداء.",
     "en": "The nominative as predicate is not available in them—indeed in any of the conditional nouns—for only a verb occurs after them, and a verb is not fit to be a mubtadaʾ."},
    {"type": "matn",
     "ar": "وما هو لازم الظرفية من هذه كـ«متى وأين وأيان وكيف وأنى وإذا» إن لم ينجر بجار نحو: «من أين» فلا بد من كونها منصوبة على الظرفية.",
     "en": "Those of these that are necessarily adverbial, such as “matā”, “ayna”, “ayyāna”, “kayfa”, “annā” and “idhā”, if not made genitive by a preposition, as in “min ayna” (from where), must be accusative as adverbs."},
    {"type": "matn",
     "ar": "وعن بعضهم: أن «إذا» قد يخرج عن الظرفية، ويقع اسما صريحا، نحو: «إذا يقوم زيد إذا يقعد عمرو» أي: وقت قيام زيد وقت قعود عمرو، فهي مرفوعة بالابتداء.",
     "en": "It is reported from some that “idhā” may leave adverbiality and occur as a plain noun, as in “idhā yaqūmu Zaydun idhā yaqʿudu ʿAmrun”, that is, “the time Zayd stands is the time ʿAmr sits”; it is then nominative as mubtadaʾ."},
    {"type": "matn",
     "ar": "وقال الشارح الرضي: وأنا لم أعثر لهذا على شاهد من كلام العرب،",
     "en": "The commentator al-Raḍī said: I have not found any attestation of this in the speech of the Arabs."},
    {"type": "matn",
     "ar": "وما هو لازم الظرفية يرتفع في الاستفهام محلا مع انتصابه على الظرفية إذا كان خبرا لمبتدأ مؤخر نحو: «متى عهدك بفلان؟» أي: «متى كائن عهدك به؟».",
     "en": "What is necessarily adverbial is nominative in position in interrogation, while being accusative as an adverb, when it is the predicate of a postponed mubtadaʾ, as in “matā ʿahduka bi-fulān?” (when did you last see so-and-so?), that is, “when is your [last] meeting with him [located]?”"},
    {"type": "matn",
     "ar": "وأما «أي» فيتأتى فيه الوجوه الأربعة كلها، فإنه قد يقع في محل الرفع بالخبرية أيضا على تقدير انتصابه على الظرفية نحو: «أي وقت مجيئك؟» أي: أي وقت كائن",
     "en": "As for “ayy”, all four possibilities are available in it, for it may also occupy the position of the nominative as a predicate, on supposing it accusative as an adverb, as in “ayya waqtin majīʾuka?” (at what time is your coming?), that is, “at what time is [your coming] located…"},

    {"type": "rule"},

    # ---------------- Footnote continued from PDF p. 403 (its footnote ٤) ----------------
    {"type": "note", "num": ""},
    {"type": "quran",
     "ar": "﴿ليلة القدر خير من ألف شهر﴾ (القدر:٣)",
     "en": "…“The Night of Decree is better than a thousand months” (Qurʾān, Sūrat al-Qadr 97:3)."},
    {"type": "pair",
     "ar": "فما قيل: ولا يخفى أن في قوله: وكذلك أسماء الشرط والاستفهام حزازة؛ لأن المراد جميع أسماء الشرط وباقي أسماء الاستفهام وهم.",
     "en": "So what has been said—“it is not hidden that there is awkwardness in his words ‘likewise the conditional and interrogative nouns’, because what is meant is all the conditional nouns and the remaining interrogative nouns”—is a mistake."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فإن «من وما» يأتي فيهما الوجوه الثلاثة، ولا يأتي فيهما الرفع على الخبرية،",
     "en": "For “man” and “mā” admit the three possibilities but not the nominative as predicate;"},
    {"type": "pair",
     "ar": "و«أي» يأتي فيها الوجوه الأربعة، و«أين ومتى وأنى وإذا وكيف وأيان» لكونها لازمة الظرفية لا يأتي فيها الرفع بالابتداء.",
     "en": "“ayy” admits all four; and “ayna”, “matā”, “annā”, “idhā”, “kayfa” and “ayyāna”, being necessarily adverbial, do not admit the nominative as mubtadaʾ."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: بالظرفية كما يدل عليه قوله: بالشرائط المذكورة، فلا ينافي ما في الرضي من تأتي الرفع فيهما على الخبرية نحو: من أنت؟ وما دينك؟",
     "en": "That is, by way of adverbiality, as indicated by his words “under the stated conditions”; so it does not conflict with what is in al-Raḍī about the nominative as predicate being available in them, as in “man anta?” (who are you?) and “mā dīnuka?” (what is your religion?)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وإذا كان اسم الشرط مبتدأ فعلى أربعة مذاهب خبره: إما الشرط والجزاء، أو الشرط فقط، فهذان ظاهرا بيان المصنف فافهم، أو الجزاء فقط، أو اسم الشرط مبتدأ لا خبر له.",
     "en": "When the conditional noun is a mubtadaʾ, there are four views on its predicate: either the condition and the apodosis (jazāʾ) together, or the condition alone—these two being the apparent sense of the author’s exposition, so understand—or the apodosis alone, or the conditional noun is a mubtadaʾ without a predicate."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سورة البقرة: ١١٠، سورة المزمل: ٢٠.",
     "en": "Qurʾān, Sūrat al-Baqara 2:110; Sūrat al-Muzzammil 73:20."},
]
