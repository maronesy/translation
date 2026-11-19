# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 128 (printed ١٢٧)."""

PAGE_NUMBER = 128
PRINTED_PAGE = "١٢٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "فاعلا، وهي: «الضمة، والواو، والألف».",
     "en": "…acting [as a marker of the nominative], namely: “the ḍamma, the wāw, and the alif.”"},
    {"type": "matn",
     "ar": "والمراد باشتمال الاسم عليها: أن يكون موصوفا بها[[١]] لفظا، أو تقديرا، أو محلا.",
     "en": "What is meant by the noun’s “bearing” them is that it be qualified by them either in wording (lafẓan), or by implication (taqdīran), or by grammatical position (maḥallan)."},
    {"type": "matn",
     "ar": "ولا شك أن الاسم موصوف بالرفع المحلي[[٢]]؛ إذ معنى الرفع المحلي أنه في محل لو كان ثمة معرب لكان مرفوعا لفظا أو تقديرا،",
     "en": "There is no doubt that the noun is qualified by nominative case by grammatical position (al-rafʿ al-maḥallī); for the meaning of positional nominative is that it occupies a position in which, were there a declinable word (muʿrab), it would be marked nominative either in wording or by implication."},
    {"type": "matn",
     "ar": "وكيف يختص الرفع[[٣]] بما عدا الرفع المحلى؟ وهو يبحث مثلا[[٤]] عن أحوال الفاعل إذا كان مضمرا متصلا، كما سيجيء.",
     "en": "So how could “nominative” be restricted to what excludes positional nominative? Indeed, he investigates, for example, the states of the fāʿil (agent) when it is a pronominal suffix attached [to its verb], as will come later."},

    {"type": "section", "ar": "[الفاعل]",
     "en": "The Agent (al-Fāʿil)"},

    {"type": "matn",
     "ar": "(فمنه) أي: من المرفوع[[٥]]، أو مما اشتمل[[٦]] على علم الفاعلية (الفاعل).",
     "en": "(And of it) — that is, of the nominative, or of that which bears the mark of agency (ʿalam al-fāʿiliyya) — (is the fāʿil, the agent)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: كالموصوف بها، فإن الحركات والحروف الإعرابية، وإن لم تكن أوصافا لكنها مشبهة بها لعدم استقلالها بالتلفظ وتبعيتها للمعرب.",
     "en": "That is: as one qualified by them; for the vowels and the letters of inflection (al-ḥurūf al-iʿrābiyya), though they are not [strictly] attributes, are yet likened to attributes, because they lack independence in utterance and are subordinate to the declinable word."},
    {"type": "pair",
     "ar": "ويجوز أن يقال: إن صيغة المرفوع كصيغة المعلوم للنسبة، فالمرفوع ما له نسبة إلى علامة الفاعلية بكونه ملابسا لها ملابسة الكل لجزئه وتضمنه له، أو ملابسة المطرو عليه للطارئ، أو المراد بالاشتمال، هو هذه الملابسة.",
     "en": "It may also be said that the form marfūʿ (raised/nominative) is, like the form maʿlūm (active), a relational form (li-l-nisba); so the marfūʿ is that which has a relation to the mark of agency by way of being conjoined with it — the conjunction of a whole with its part and its inclusion of it, or the conjunction of that upon which something supervenes with what supervenes upon it. Alternatively, what is meant by “bearing” is this very conjunction."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "رد لما حققه الفاضل الهندي في هذا المقام حيث قال: الإعراب المحلي لا يشتمل عليه اللفظ، فلا يكون هؤلاء في «جاءني هؤلاء» مرفوعا؛ إذ معنى الرفع المحلي أنه في محل لو كان ثمة اسم معرب لكان مرفوعا، هذا كلامه.",
     "en": "A refutation of what the learned al-Fāḍil al-Hindī established in this connection, where he said: positional inflection is not borne by the wording, so hāʾulāʾi in “hāʾulāʾi came to me” is not [truly] marfūʿ; for the meaning of positional nominative is that it occupies a position in which, were there a declinable noun, it would be marfūʿ — this is his statement."},
    {"type": "pair",
     "ar": "فلم يرد بذاك أن المرفوع وما اشتمل على الرفع لا يشتملانه، بل أراد أن شمولهما له ليس إلا بضرب من المسامحة الشائعة.",
     "en": "By this he did not mean that “the marfūʿ” and “that which bears the nominative” do not encompass it; rather he meant that their encompassing it is only by a kind of common laxity of expression (musāmaḥa)."},
    {"type": "pair",
     "ar": "ولقد تعرض الشارح بالفاضل، بل شنع عليه تشنيعا لطيفا بأن دليلك يثبت نقيض دعواك؛ لأن الاسم موصوف بالرفع المحلي، فيكون مشتملا على الرفع محلا كما أنه باعتبار اتصافه بالرفع اللفظي مشتمل على الرفع لفظا.",
     "en": "The commentator [Jāmī] took the Fāḍil to task — indeed, he subtly censured him — [saying]: “your own proof establishes the contradictory of your claim, since the noun is qualified by positional nominative, and so bears the nominative positionally, just as, in respect of its being qualified by verbal nominative, it bears the nominative in wording.”"},
    {"type": "pair",
     "ar": "ولا يخفى أن الفاضل ليس في معرض هذا التعرض؛ لأن الاتصاف بالرفع المحلي يوجب البراءة عن الرفع حقيقة، والاشتمال عليه حكما.",
     "en": "Yet it is not hidden that the Fāḍil is not exposed to this rebuke; for being qualified by positional nominative entails freedom from the nominative in reality, while bearing it holds only in ruling (ḥukman)."},
    {"type": "pair",
     "ar": "ومقصوده التنبيه على عدم الاشتمال حقيقة.",
     "en": "His aim was only to draw attention to the absence of real bearing [of the nominative]."},
    {"type": "pair",
     "ar": "ولك أن تقول: إن مقصود الشارح أيضا هو التنبيه على كون الاسم موصوفا بالرفع المحلي، وداخلا في المرفوع وإن خلا عن الرفع حقيقة، وليس مقصوده التعرض بالفاضل.",
     "en": "You may [in turn] say: the commentator’s aim, too, is to draw attention to the noun’s being qualified by positional nominative and included among the marfūʿāt, even though it is void of the nominative in reality — his aim being not to rebuke the Fāḍil."},
    {"type": "pair",
     "ar": "فإن قلت: المعرب محلا هل هو معرب بالحركة أو بالحروف، وهو بحيث لو فرض في محله المعرب بالحرف كان معربا بالحرف، ولو فرض المعرب بالحركة كان معربا بالحركة؟",
     "en": "Now if you ask: is that which is inflected positionally inflected by a vowel or by letters — such that, were one supposes in its place a word inflected by a letter it would be inflected by a letter, and were one to suppose a word inflected by a vowel it would be inflected by a vowel?"},
    {"type": "pair",
     "ar": "قلت: الأقرب بالاعتبار أن يجعل مثل الذي معربا بالحركة محلا، ومثل «اللذان واللذين» معربا بالحرف محلا.",
     "en": "I say: the more fitting view is to reckon a word like alladhī as inflected by a vowel positionally, and a word like “al-ladhāni / al-ladhayni” as inflected by a letter positionally."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لعل الباعث على التخصيص عدم ظهور اشتمال الاسم على علم الفاعلية، أو جعل اللام للعهد.",
     "en": "Perhaps what prompted the restriction is that the noun’s bearing of the mark of agency is not manifest, or [that it comes from] taking the definite article (lām) as one of specific reference (al-ʿahd)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "ليس تخصيص الرفع بما عدا المحلي مع البحث عن أحوال الفاعل المبني بتلك المثابة من الاستبعاد لجواز أن يكون البحث عنه تقريبيا، ومثله غير نادر في كتب العلوم.",
     "en": "The restriction of “nominative” to what excludes the positional, together with investigating the states of the indeclinable (mabnī) agent, is not so far-fetched [as alleged], since the investigation of it may be approximate; and the like of this is not rare in scholarly books."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فإن الكلام مسوق له. و«من» ابتدائية اتصالية.",
     "en": "For the discourse is directed to it. And “min” here is one of inception and connection (ibtidāʾiyya ittiṣāliyya)."},
    {"type": "pair",
     "ar": "ويأبى عنه قوله: «ومنها المبتدأ»؛ لأن الضمير فيه راجع إلى المرفوعات، ومن تبعيضية.",
     "en": "But his statement “and among them is the mubtadaʾ” resists this [reading], because the pronoun in it refers back to the marfūʿāt (nominatives), and [there] min is partitive (tabʿīḍiyya)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لقربه. ويجوز أن يجعل راجعا إلى المرفوعات بضرب من التأويل كالمذكور والقسم الأول والجمع والقبيل، ويوافقه قوله: «ومنها المبتدأ».",
     "en": "Because of its nearness. It may also be made to refer back to the marfūʿāt by a kind of interpretation — like “the aforementioned,” “the first category,” “the assembly,” or “the class” — and his statement “and among them is the mubtadaʾ” accords with this."},
]
