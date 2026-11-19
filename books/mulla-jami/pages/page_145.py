# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 145 (printed ١٤٤)."""

PAGE_NUMBER = 145
PRINTED_PAGE = "١٤٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(و) يختار النحاة (الكوفيون إعمال الأول) أي: إعمال الفعل الأول مع تجويز إعمال الثاني لسبقه، وللاحتراز عن الإضمار قبل الذكر[[١]].",
     "en": "(And the Kūfan) grammarians choose (to make the first govern—wa-l-kūfiyyūn iʿmāl al-awwal), that is: to make the first verb govern, while allowing the second to be made to govern, because of its precedence, and to avoid concealment before mention (al-iḍmār qabl al-dhikr)."},
    {"type": "matn",
     "ar": "(فإن أعملت) الفعل (الثاني) كما هو مذهب البصريين، وبدأ به؛ لأنه المذهب المختار الأكثر استعمالا",
     "en": "(So if you make) the (second) verb (govern—fa-in aʿmalta al-thānī), as is the doctrine of the Baṣrans—and he began with it because it is the preferred doctrine, the more frequent in usage—"},
    {"type": "matn",
     "ar": "(أضمرت الفاعل في) الفعل (الأول) إذا اقتضى الفاعل؛",
     "en": "(you conceal the agent in the first) verb (aḍmarta al-fāʿila fī al-awwal), when it requires the agent;"},
    {"type": "matn",
     "ar": "لجواز الإضمار قبل الذكر في العمدة بشرط التفسير، وللزوم التكرار بالذكر[[٢]] وامتناع الحذف",
     "en": "because concealment before mention is permissible in an indispensable constituent (ʿumda) on condition of [subsequent] explication, and because mentioning [it] entails repetition, and elision is precluded,"},
    {"type": "matn",
     "ar": "(على وفق) الاسم (الظاهر[[٣]]) الواقع بعد الفعلين، أي: على موافقته إفرادا وتثنية وجمعا وتذكيرا وتأنيثا؛",
     "en": "(in accordance with the overt) noun (ʿalā wafqi al-ẓāhir) occurring after the two verbs, that is: in agreement with it in singular, dual and plural, and in masculine and feminine;"},
    {"type": "matn",
     "ar": "لأنه مرجع الضمير، والضمير يجب[[٤]] أن يكون موافقا للمرجع في هذه الأمور",
     "en": "because it is the referent of the pronoun, and the pronoun must agree with the referent in these matters"},
    {"type": "matn",
     "ar": "(دون الحذف[[٥]])؛ لأنه لا يجوز حذف الفاعل إلا إذا سد شيء مسده",
     "en": "(not by elision—dūna al-ḥadhf); because elision of the agent is not permissible unless something takes its place,"},
    {"type": "matn",
     "ar": "(خلافا للكسائي[[٦]])، فإنه لا يضمر الفاعل بل يحذفه تحرزا عن الإضمار قبل الذكر.",
     "en": "(contrary to al-Kisāʾī—khilāfan li-l-Kisāʾī), for he does not conceal the agent but elides it, guarding against concealment before mention."},
    {"type": "matn",
     "ar": "ويظهر أثر الخلاف في نحو: «ضرباني وأكرمني الزيدان» عند البصريين، و«ضربني وأكرمني الزيدان» عند الكسائي.",
     "en": "The effect of the disagreement appears in such as: “The two Zayds struck me and honored me” (ḍarabānī wa-akramanī al-Zaydān) according to the Baṣrans, and “ḍarabanī wa-akramanī al-Zaydān” according to al-Kisāʾī."},
    {"type": "matn",
     "ar": "(وجاز[[٧]]) أي: إعمال الفعل الثاني مع اقتضاء الفعل الأول الفاعل[[٨]]",
     "en": "(And it is permissible—wa-jāza), that is: making the second verb govern while the first verb requires the agent,"},
    {"type": "matn",
     "ar": "(خلافا للفراء)، فإنه لا يجوز إعمال الفعل الثاني عند اقتضاء الفعل الأول الفاعل؛ لأنه يلزم",
     "en": "(contrary to al-Farrāʾ—khilāfan li-l-Farrāʾ), for [according to him] making the second verb govern is not permissible when the first verb requires the agent; because it entails…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فينبغي أن يقول: وحذف الفاعل والتكرار.",
     "en": "So he ought to say: “and [to avoid] elision of the agent and repetition.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: بالإظهار، يعني: أن في معمول الفعل الأول عند إعمال الثاني ثلاث احتمالات: الإضمار، والحذف، والذكر.",
     "en": "That is: by making [it] overt. He means: in the governed element of the first verb, when the second is made to govern, there are three possibilities: concealment, elision and mention."},
    {"type": "pair",
     "ar": "فاختاروا الإضمار لجوازه في العمدة، ولم يختاروا الحذف؛ لأنه يلزم حذف الفاعل من غير أن يسد شيء مسده،",
     "en": "They chose concealment because it is permissible in an indispensable constituent; they did not choose elision, because it entails eliding the agent without anything taking its place;"},
    {"type": "pair",
     "ar": "ولم يختاروا ذكر الفاعل؛ لأنه يوجب تكرار اللفظ.",
     "en": "and they did not choose mentioning the agent, because it necessitates repetition of the expression."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "حال من الفاعل، أي: على وفق لفظه، أو على وفق معناه كأن يكون الفاعل لفظ \"نفس\"، وتريد به مذكرا.",
     "en": "A ḥāl of the agent; that is: in accordance with its wording, or in accordance with its meaning—as when the agent is the word “nafs” (soul, a feminine noun) and you intend by it a male."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أراد بالضمير جنسه، فلذا أظهر في موضع الإضمار.",
     "en": "By “the pronoun” he meant its genus; that is why he used an overt noun where a pronoun would be expected."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "صرح به ليرتبط به قوله: \"خلافا للكسائي\"، ولهذا لم يذكر \"ودون الإضمار\"؛ لأنه لم يذهب إليه أحد.",
     "en": "He stated it explicitly so that his words “contrary to al-Kisāʾī” would be connected to it; and for this reason he did not mention “and not by concealment,” because no one has held that."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أصله يخالف قوله: الإضمار قول الكسائي خلافا.",
     "en": "Its underlying form: his statement, “concealment,” opposes the statement of al-Kisāʾī, an opposing (khilāfan)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "الجملة اعتراضية ذكرت لبيان قول الفراء.",
     "en": "The sentence is parenthetical, mentioned to explain the view of al-Farrāʾ."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "الأولى أن يضم إلى هذا الكلام قولنا: وإضمار الفاعل في الفعل الأول عند الجمهور وحذف الفاعل عن الأول عند الكسائي.",
     "en": "It would be better to add to this statement our words: “and [with] concealment of the agent in the first verb according to the majority, and elision of the agent from the first according to al-Kisāʾī.”"},
    {"type": "pair",
     "ar": "ثم يقول خلافا للفراء، فإن الخلاف يتعلق بجميعها،",
     "en": "Then he would say “contrary to al-Farrāʾ,” for the disagreement concerns all of them;"},
    {"type": "pair",
     "ar": "ولا يرتبط دليله أعني: قوله: لأنه يلزم على تقدير إعماله إما الإضمار قبل الذكر أو حذف الفاعل إلا بملاحظة ما ذكرنا،",
     "en": "and his proof—I mean his words “because on the supposition of making it govern, either concealment before mention or elision of the agent is entailed”—is not connected [to the claim] except by taking account of what we have mentioned;"},
    {"type": "pair",
     "ar": "فإن بمجرد إعمال الثاني لا يلزم الإضمار قبل الذكر في الأول، أو حذف الفاعل فيه، فلا بد من تقييد إعمال الثاني بهذين القيدين.",
     "en": "for the mere making of the second govern does not entail concealment before mention in the first, or elision of the agent in it; so making the second govern must be qualified by these two qualifications."},
]
