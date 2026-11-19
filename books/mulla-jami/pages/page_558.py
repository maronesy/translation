# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 558 (printed ٥٥٧)."""

PAGE_NUMBER = 558
PRINTED_PAGE = "٥٥٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(وقالوا: «لولا أنك»[[١]]) بفتح الهمزة بعد «لولا» الامتناعية؛ (لأنه) أي: ما بعد «لولا» الامتناعية (مبتدأ) وكون المبتدأ مفردا واجب نحو: «لولا أنك منطلق انطلقت».",
     "en": "(And they said “law-lā annaka”) with fatḥa on the hamza after the “law-lā” of prevention (al-imtināʿiyya), (because it), that is, what follows the law-lā of prevention, (is a subject), and a subject must be a single term, as in “law-lā annaka munṭaliqun la-nṭalaqtu (were it not that you are leaving, I would have left)”."},
    {"type": "matn",
     "ar": "وكذلك بعد «لولا» التحضيضية؛ لأنها مع اسمها وخبرها بعدها معمول للفعل[[٢]] الواجب دخول «لولا»[[٣]] التحضيضية عليه،",
     "en": "Likewise after the law-lā of incitement (al-taḥḍīḍiyya), because after it [anna] together with its noun and predicate is governed by the verb upon which the law-lā of incitement must enter,"},
    {"type": "matn",
     "ar": "نحو: «لولا أني معاذ لك زعمت» أي: لولا زعمت أني معاذ لك، و«لولا أنك ضربتني صدر منك» أي: لولا صدر الضرب منك أنك ضربتني.",
     "en": "as in “law-lā annī maʿādhun laka zaʿamta”, that is, “why did you not claim that I am a refuge for you?”, and “law-lā annaka ḍarabtanī ṣadara minka”, that is, “why did there not issue from you the striking, that you struck me?”"},
    {"type": "matn",
     "ar": "(وكذلك) قالوا: (لو أنك) بفتح الهمزة؛ (لأنه) أي: ما بعد «لو» (فاعل) لفعل محذوف، والفاعل يجب أن يكون مفردا: نحو: «لو أنك قائم»[[٤]] أي: لو وقع قيامك.",
     "en": "(And likewise) they said (“law annaka”) with fatḥa on the hamza, (because it), that is, what follows “law”, (is an agent) of an elided verb, and the agent must be a single term, as in “law annaka qāʾimun”, that is, “if your standing occurred”."},
    {"type": "matn",
     "ar": "(فإن جاز[[٥]]) في موضع (التقديران[[٦]]) أي: تقدير المفرد وتقدير الجملة (جاز الأمران) أي: الفتح والكسر في «أن»",
     "en": "(So if) in some position (both construals are admissible), that is, construal as a single term and construal as a sentence, (both options are admissible), that is, fatḥa and kasra in “anna”:"},
    {"type": "matn",
     "ar": "الفتح على تقدير جعل «أن» مع اسمها وخبرها مفردا، والكسر على تقدير جعلها معهما جملة (مثل: «من يكرمني فإني أكرمه») مما وقع بعد الفاء الجزائية.",
     "en": "fatḥa on the construal that “anna” with its noun and predicate is a single term, and kasra on the construal that it with them is a sentence; (as in “man yukrimunī fa-innī ukrimuhu (whoever honours me, I shall honour him)”), among cases occurring after the fāʾ of the apodosis (al-fāʾ al-jazāʾiyya)."},
    {"type": "matn",
     "ar": "فإن كان المراد: «من يكرمني فأنا أكرمه» وجب الكسر؛ لأنها وقعت في موضع الجملة،",
     "en": "If what is meant is “man yukrimunī fa-anā ukrimuhu (whoever honours me, I honour him)”, kasra is required, because it occurs in the position of a sentence;"},
    {"type": "matn",
     "ar": "وإن كان المراد: «من يكرمني فجزاؤه أني أكرمه، أو إكرامي ثابت له»، وجب الفتح؛ لأنها وقعت في موضع المفرد، لأنها إما مبتدأ أو خبر مبتدأ[[٧]].",
     "en": "and if what is meant is “whoever honours me, his recompense is that I honour him”, or “my honouring is established for him”, fatḥa is required, because it occurs in the position of a single term, since it is either a subject or the predicate of a subject."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "خص ذكر «لولا» و«لو» بالتعرض ردا على المخالف،",
     "en": "He singled out “law-lā” and “law” for mention in order to refute the opposing view;"},
    {"type": "pair",
     "ar": "فإن المبرد والكسائي زعما أن ما بعد «لولا» فاعل. وزعم الكوفيون أن ما بعد حرف الشرط مبتدأ.",
     "en": "for al-Mubarrad and al-Kisāʾī claimed that what follows “law-lā” is an agent, and the Kūfans claimed that what follows the conditional particle is a subject."},
    {"type": "pair",
     "ar": "وقد بعد الشيخ الرضي حيث جعل قوله: وقالوا: لولا أنك جواب سؤال مقدر، وهو أنه يجب بعد «لولا» جملة اسمية، فيجب كسر «إن» ليكون الجملة اسمية؛",
     "en": "Shaykh al-Raḍī went far when he made his words “and they said: law-lā annaka” the answer to an implied question, namely: a nominal sentence is required after “law-lā”, so “inna” should be read with kasra for the sentence to be nominal."},
    {"type": "pair",
     "ar": "لأنه مع غاية ضعف السؤال؛ لأنه عرف سابقا أن خبر المبتدأ بعد «لولا» محذوف قطعا، وأن المفتوحة لا توجب الفعلية",
     "en": "[He went far] because, besides the extreme weakness of the question — since it was learned earlier that the predicate of the subject after “law-lā” is invariably elided, and that the fatḥa form does not entail a verbal sentence —"},
    {"type": "pair",
     "ar": "لا يساعده قوله: ولو أنك، لأنه فاعل، لأنه لا سؤال لدفعه.",
     "en": "his words “and law annaka, because it is an agent” do not support it, since there is no question for it to rebut."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فاعلا كان أو مفعولا، ولذا أورد مثالين.",
     "en": "Whether as agent or as object; this is why he gave two examples."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لأن التحضيض إنما يكون على معاني الأفعال دون الأسماء والحروف.",
     "en": "Because incitement (taḥḍīḍ) bears only on the meanings of verbs, not of nouns and particles."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "صوابه: لو أنك قمت كما ستعرفه في بحث حروف الشرط.",
     "en": "The correct form is “law annaka qumta (if you had stood)”, as you will learn in the discussion of the conditional particles."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    # REVIEW: printed «إشارة إلا أنه»; «إلى» is expected — transcribed as printed.
    {"type": "pair",
     "ar": "أورد الفاء إشارة إلا أنه متفرع على القاعدة السابقة،",
     "en": "He used the fāʾ to indicate that it is a corollary of the preceding rule."},
    {"type": "pair",
     "ar": "ومعنى جواز التقديرين أن يكون كل واحد منهما مؤديا للمعنى المقصود من غير تفاوت.",
     "en": "The meaning of the admissibility of both construals is that each of them conveys the intended meaning without difference."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    # REVIEW: printed «جواب الآخر»; «جواز الآخر» is expected — transcribed as printed; translated by sense.
    {"type": "pair",
     "ar": "ترجيح أحدهما بعدم تكلف الحذف لا ينافي جواب الآخر،",
     "en": "Preferring one of them for not requiring a strained elision does not exclude the admissibility of the other;"},
    {"type": "pair",
     "ar": "فلا يرد أنه كيف يجوز الفتح المحتاج إلى الحذف في «من يكرمني فإني أكرمه»، ونظائره مع صحة الكسر المستغنى عن الحذف.",
     "en": "so the objection does not arise: how can fatḥa, which requires an elision, be admissible in “man yukrimunī fa-innī ukrimuhu” and its like, when kasra, which dispenses with elision, is sound?"},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "اقتصر الرضي على الأول، والثاني من زوائد الشارح.",
     "en": "Al-Raḍī confined himself to the first; the second is one of the commentator’s additions."},
    {"type": "pair",
     "ar": "وكان الرضي لم يلتفت إليه لاستلزامه الحذف قبل الحاجة،",
     "en": "It seems al-Raḍī paid no attention to it because it entails elision before there is need for it."},
    {"type": "pair",
     "ar": "لكن في كونه مبتدأ بحث؛ لأنهم لما وجبوا تقديم الخبر لئلا يلتبس المفتوحة بالمكسورة، فكيف يجوز حذفه، وحذفه يوجب الالتباس كالتأخير بالجملة.",
     "en": "But its being a subject is open to discussion: since they made it obligatory to put the predicate first, so that the fatḥa form is not confused with the kasra form, how can its elision be admissible, when its elision causes confusion, just as postponing it does, all in all?"},
    {"type": "pair",
     "ar": "قوله: وإكرامي ثابت له يوهم تقدير الخبر مؤخرا، وهو لا يجوز؛ لأن المقام مقام وجوب تقديم الخبر.",
     "en": "His words “and my honouring is established for him” suggest construing the predicate as placed after, which is not admissible, because the context is one in which the predicate must come first."},
]
