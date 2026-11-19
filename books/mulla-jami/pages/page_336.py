# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 336 (printed ٣٣٥)."""

PAGE_NUMBER = 336
PRINTED_PAGE = "٣٣٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «… (بالنسبة) الواقعة في الكلام.» at the foot of PDF p. 335 (new sentence).
    {"type": "matn",
     "ar": "فقوله: «بالنسبة» متعلق بالقصد المفهوم من المقصود (مع متبوعه)",
     "en": "His words “by the attribution” are attached to the intending understood from “intended”; (together with the noun it follows) (maʿa matbūʿihi),"},
    {"type": "matn",
     "ar": "أي: كما يكون هو مقصودا بتلك النسبة يكون متبوعه أيضا مقصودا بها نحو: «جاءني زيد وعمرو»،",
     "en": "that is, just as it is intended by that attribution, the noun it follows is also intended by it, as in “jāʾanī Zaydun wa-ʿAmrun” (Zayd and ʿAmr came to me);"},
    {"type": "matn",
     "ar": "فـ«عمرو» تابع؛ لأنه معطوف على «زيد» قصد نسبة المجيء إليه بنسبة المجيء الواقعة في الكلام،",
     "en": "for “ʿAmr” is a dependent, since it is conjoined to “Zayd”, and the attribution of coming to it is intended by the attribution of coming that occurs in the utterance;"},
    {"type": "matn",
     "ar": "وكما أن نسبة المجيء إليه مقصودة كذلك نسبته إلى «زيد» الذي هو متبوعه أيضا مقصودة.",
     "en": "and just as the attribution of coming to it is intended, so too its attribution to “Zayd”, which is the noun it follows, is intended."},
    {"type": "matn",
     "ar": "فقوله: «مقصود بالنسبة» احتراز عن غير البدل[[١]] من التوابع؛ لأنها غير مقصودة[[٢]]، بل المقصود متبوعاتها.",
     "en": "His words “intended by the attribution” exclude the dependents other than the substitute (badal), for they are not intended; rather, what is intended is the nouns they follow."},
    {"type": "matn",
     "ar": "وقوله: «مع متبوعه» احتراز عن البدل؛ لأنه المقصود دون متبوعه.",
     "en": "His words “together with the noun it follows” exclude the substitute, for it is what is intended, not the noun it follows."},
    {"type": "matn",
     "ar": "قيل: يخرج بقوله: «مع متبوعه» المعطوف بـ«لا، وبل، ولكن، وأم، وأما، وأو»؛ لأن المقصود بالنسبة معها أحد الأمرين من التابع والمتبوع لا كلاهما.",
     "en": "It has been said: by his words “together with the noun it follows” the noun conjoined by “lā”, “bal”, “lākin”, “am”, “immā” and “aw” is excluded, since with them what is intended by the attribution is one of the two, the dependent or the followed, not both."},
    {"type": "matn",
     "ar": "وأجيب[[٣]]: بأن المراد بكون المتبوع مقصودا بالنسبة ألا يذكر لتوطئة ذكر التابع،",
     "en": "It has been answered that what is meant by the followed noun’s being intended by the attribution is that it is not mentioned merely to pave the way for mentioning the dependent,"},
    {"type": "matn",
     "ar": "وبكون التابع مقصودا بالنسبة ألا يكون كالفرع على المتبوع من غير استقلال به،",
     "en": "and by the dependent’s being intended by the attribution, that it is not like a branch of the followed noun without independence of its own;"},
    {"type": "matn",
     "ar": "ولا شك أن المعطوف والمعطوف عليه بتلك الحروف الستة مقصودان بالنسبة معا بهذا المعنى.",
     "en": "and there is no doubt that the conjoined noun and the noun conjoined to by those six particles are both intended by the attribution together in this sense."},
    {"type": "matn",
     "ar": "ولما تم الحد بما ذكره[[٤]] جمعا ومنعا أردفه لزيادة التوضيح بقوله: (يتوسط بينه[[٥]])",
     "en": "Since the definition was complete, comprehensive and exclusive, with what he had mentioned, he followed it up, for further clarification, with his words: (there intervenes between it)…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لأنها لم تنسب إليها شيء ولا هي إلى شيء؛ لأن نسبتها غير مقصودة كالمبدل منه،",
     "en": "Because nothing is attributed to them, nor are they attributed to anything, since their attribution is not intended, like the noun substituted for (al-mubdal minhu);"},
    # REVIEW: «فلا تمل» printed; perhaps for «فتأمل»; transcribed as printed.
    {"type": "pair",
     "ar": "فإدراج القصد ليس لقصد الاحتراز عن غير البدل، بل لبيان المشترك بينه وبين البدل، فاعرف القصد، فلا تمل.",
     "en": "so the inclusion of intending is not meant to exclude what is other than the substitute, but to state what it shares with the substitute. So know the intent, and do not deviate."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "بل المقصود متبوعاتها. وذلك لأنك تبين بالوصف المتبوع بذكر معنى فيه، وتوضح بعطف البيان المتبوع بذكر أشهر اسميه،",
     "en": "Rather, what is intended is the nouns they follow. That is because by the qualifier (waṣf) you make the followed noun clear by mentioning a meaning in it; by the explicative apposition (ʿaṭf al-bayān) you clarify the followed noun by mentioning the better known of its two names;"},
    {"type": "pair",
     "ar": "وتبين بالتأكيد أن المنسوب إليه بحسب الظاهر هو المنسوب إليه في الحقيقة لا غير،",
     "en": "and by the corroborative (taʾkīd) you make clear that what is apparently the subject of attribution is in reality the subject of attribution and nothing else,"},
    {"type": "pair",
     "ar": "أي: لم يقع غلط، ولا مجاز في النسبة، أو أن المذكور بلفظ العموم باق على عمومه.",
     "en": "that is, no error has occurred and there is no figurative usage (majāz) in the attribution; or that what is mentioned with a general expression remains general."},
    {"type": "pair",
     "ar": "ولا شك أنك إذا بينت شيئا بشيء، فالمقصود هو المبين، والبيان فرعه.",
     "en": "There is no doubt that when you make one thing clear by another, what is intended is the thing made clear, and the clarification is its branch."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فهم هذا المعنى من كون العطف مقصودا بالنسبة إلى متبوعه بعيد جدا على أنه يرد عليه أن بدل الغلط مقصود بالنسبة مع متبوعه بهذا المعنى.",
     "en": "Understanding this meaning from the conjoined noun’s being intended by the attribution [together] with the noun it follows is very far-fetched; moreover, the objection arises against it that the substitute of error (badal al-ghalaṭ) is intended by the attribution together with the noun it follows in this sense."},
    {"type": "pair",
     "ar": "وبالجملة لا فرق في المعنى بين قولنا: «جاءني زيد حماره» وبين قولنا: «جاءني زيد بل حماره»، فجعل أحدهما داخلا في مفهوم التعريف بهذا التفسير دون الآخر تحكم.",
     "en": "In short, there is no difference in meaning between our saying “jāʾanī Zaydun ḥimāruhu” (Zayd—his donkey—came to me) and our saying “jāʾanī Zaydun bal ḥimāruhu” (Zayd, no, his donkey, came to me); so to make one of them fall under the concept of the definition by this interpretation, and not the other, is arbitrary."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يحتمل معنيين: أحدهما: أن قوله: يتوسط حكم خارج عن التعريف، وأخر المثال عنه أعني: قوله: مثل قام زيد وعمرو؛",
     "en": "It admits two meanings. The first: that his words “there intervenes” are a ruling outside the definition, and he placed the example after it, I mean his words “as in qāma Zaydun wa-ʿAmrun”,"},
    {"type": "pair",
     "ar": "لأنه يوجب زيادة توضيح، فكأنه من تتمة التعريف، أو لأنه قصد تمثيل الحكم أيضا.",
     "en": "because it brings further clarification, so that it is as if part of the completion of the definition; or because he intended to exemplify the ruling as well."},
    {"type": "pair",
     "ar": "وثانيهما: أنه داخل في التعريف كما ينساق إليه الفهم. ويؤيده تأخير المثال،",
     "en": "The second: that it is part of the definition, as the understanding is led to take it; and the placing of the example after it supports this;"},
    {"type": "pair",
     "ar": "لكن ليس له دخل في المنع والجمع كما مر نظير ذلك في تعريف الإعراب.",
     "en": "but it has no share in [the definition’s] exclusiveness and comprehensiveness, as a parallel to this has passed in the definition of iʿrāb."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    # REVIEW: printed «الأظهر يقع، فكأنه فيه تجريدا»; the sense seems to be that «يقع» would be more evident than «يتوسط»; transcribed as printed.
    {"type": "pair",
     "ar": "الأظهر يقع، فكأنه فيه تجريدا.",
     "en": "“Occurs” (yaqaʿu) would be more evident; so it is as though there is abstraction (tajrīd) in it."},
]
